document.getElementById("contact-form").addEventListener("submit", function (e) {
  e.preventDefault();
  alert("Thank you for reaching out! I’ll get back to you soon.");
  this.reset();
});

// Enable search button and input functionality
function handleSearch(query) {
  if(query) {
    // Check for section navigation
    const lower = query.toLowerCase();
    if(['education','education section','#education'].includes(lower)) {
      location.hash = '#education';
      return;
    }
    if(['about','about me','#about'].includes(lower)) {
      location.hash = '#about';
      return;
    }
    if(['skills','skills section','#skills'].includes(lower)) {
      location.hash = '#skills';
      return;
    }
    if(['projects','projects section','#projects'].includes(lower)) {
      location.hash = '#projects';
      return;
    }
    if(['certificates','certifications','#certificates'].includes(lower)) {
      location.hash = '#certificates';
      return;
    }
    if(['achievements','achievements section','#achievements'].includes(lower)) {
      location.hash = '#achievements';
      return;
    }
    if(['internships','internship','#internships'].includes(lower)) {
      location.hash = '#internships';
      return;
    }
    if(['research','publications','research and publications','#research'].includes(lower)) {
      location.hash = '#research';
      return;
    }
    if(['contact','contact me','#contact'].includes(lower)) {
      location.hash = '#contact';
      return;
    }
    alert('You searched for: ' + query);
  } else {
    alert('Please enter a search term.');
  }
}

window.addEventListener('DOMContentLoaded', function() {
  var searchBtn = document.querySelector('.search-btn');
  var searchInput = document.querySelector('.search-input');
  if(searchBtn && searchInput) {
    searchBtn.addEventListener('click', function(e) {
      e.preventDefault();
      handleSearch(searchInput.value.trim());
    });
    searchInput.addEventListener('keydown', function(e) {
      if(e.key === 'Enter') {
        e.preventDefault();
        handleSearch(this.value.trim());
      }
    });
  }

  // Contact form logic
  var contactForm = document.getElementById('contact-form');
  var successMsg = document.getElementById('contact-success');
  var errorMsg = document.getElementById('contact-error');
  if(contactForm && successMsg) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      var name = document.getElementById('name').value;
      var email = document.getElementById('email').value;
      var message = document.getElementById('message').value;
      if(window.emailjs) {
        emailjs.send('YOUR_SERVICE_ID', 'YOUR_TEMPLATE_ID', {
          from_name: name,
          from_email: email,
          message: message
        })
        .then(function(response) {
          contactForm.reset();
          successMsg.style.display = 'block';
          if(errorMsg) errorMsg.style.display = 'none';
          setTimeout(function() { successMsg.style.display = 'none'; }, 4000);
        }, function(error) {
          if(errorMsg) errorMsg.style.display = 'block';
          successMsg.style.display = 'none';
          setTimeout(function() { errorMsg.style.display = 'none'; }, 4000);
        });
      } else {
        // fallback: just show success
        contactForm.reset();
        successMsg.style.display = 'block';
        if(errorMsg) errorMsg.style.display = 'none';
        setTimeout(function() { successMsg.style.display = 'none'; }, 4000);
      }
    });
  }

  // Theme toggle logic
  var themeBtn = document.getElementById('theme-toggle-btn');
  var themeIcon = document.getElementById('theme-icon');
  var dark = false;
  function setTheme(isDark) {
    if(isDark) {
      document.body.classList.add('dark-theme');
      if(themeIcon) {
        themeIcon.textContent = '☀️';
        themeIcon.title = 'Switch to Light Theme';
      }
    } else {
      document.body.classList.remove('dark-theme');
      if(themeIcon) {
        themeIcon.textContent = '🌙';
        themeIcon.title = 'Switch to Dark Theme';
      }
    }
  }
  if(themeBtn && themeIcon) {
    themeBtn.addEventListener('click', function() {
      dark = !dark;
      setTheme(dark);
    });
  }

  // Certificate toggles (Accomplishments)
  var certToggles = [
    { btn: 'show-cert-btn', panel: 'cert-options' },
    { btn: 'show-network-cert-btn', panel: 'network-cert-options' },
    { btn: 'show-fullstack-cert-btn', panel: 'fullstack-cert-options' },
    { btn: 'show-hackathon-cert-btn', panel: 'hackathon-cert-options' }
  ];
  certToggles.forEach(function(ref) {
    var btn = document.getElementById(ref.btn);
    var panel = document.getElementById(ref.panel);
    if(btn && panel) {
      btn.addEventListener('click', function() {
        panel.style.display = panel.style.display === 'flex' ? 'none' : 'flex';
      });
    }
  });

  // ========== Resume Builder Functionality ==========
  var openResumeBuilderBtn = document.getElementById('open-resume-builder');
  var resumeModal = document.getElementById('resume-modal');
  var downloadPdfBtn = document.getElementById('download-pdf-btn');
  var skillsContainer = document.getElementById('skills-container');

  if(openResumeBuilderBtn) {
    openResumeBuilderBtn.addEventListener('click', function(e) {
      e.preventDefault();
      resumeModal.style.display = 'block';
      loadSkills();
    });
  }

  // Close modal when clicking outside of it
  window.addEventListener('click', function(e) {
    if(e.target === resumeModal) {
      resumeModal.style.display = 'none';
    }
  });

  // Load available skills from backend
  function loadSkills() {
    fetch('/api/skills')
      .then(response => response.json())
      .then(data => {
        if(data.success && data.skills) {
          displaySkills(data.skills);
        }
      })
      .catch(error => {
        console.error('Error loading skills:', error);
        skillsContainer.innerHTML = '<p style="color: red;">Error loading skills. Please try again.</p>';
      });
  }

  // Display skills as checkboxes
  function displaySkills(skillsObj) {
    skillsContainer.innerHTML = '';
    
    const allSkillsMap = flattenSkills(skillsObj);
    
    allSkillsMap.forEach(skill => {
      const skillId = 'skill-' + skill.replace(/\s+/g, '-').toLowerCase();
      const skillCheckbox = document.createElement('input');
      skillCheckbox.type = 'checkbox';
      skillCheckbox.id = skillId;
      skillCheckbox.className = 'skill-checkbox';
      skillCheckbox.value = skill;
      
      const skillLabel = document.createElement('label');
      skillLabel.htmlFor = skillId;
      skillLabel.className = 'skill-label';
      skillLabel.textContent = skill;
      
      skillsContainer.appendChild(skillCheckbox);
      skillsContainer.appendChild(skillLabel);
    });
  }

  // Flatten nested skills object into single array
  function flattenSkills(skillsObj) {
    const allSkills = [];
    for(const category in skillsObj) {
      if(Array.isArray(skillsObj[category])) {
        allSkills.push(...skillsObj[category]);
      }
    }
    return allSkills;
  }

  // Get selected skills
  function getSelectedSkills() {
    const checkboxes = document.querySelectorAll('.skill-checkbox:checked');
    return Array.from(checkboxes).map(cb => cb.value);
  }

  // Generate and download resume
  if(downloadPdfBtn) {
    downloadPdfBtn.addEventListener('click', function() {
      const selectedSkills = getSelectedSkills();
      
      if(selectedSkills.length === 0) {
        alert('Please select at least one skill');
        return;
      }

      // Disable button and show loading state
      downloadPdfBtn.disabled = true;
      downloadPdfBtn.textContent = 'Generating...';

      // Call backend to generate resume
      fetch('/api/generate-resume', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          skills: selectedSkills
        })
      })
      .then(response => response.json())
      .then(data => {
        if(data.success && data.filename) {
          // Download the generated file
          window.location.href = '/api/download-resume/' + data.filename;
          
          // Close modal after a brief delay
          setTimeout(() => {
            resumeModal.style.display = 'none';
            // Reset button
            downloadPdfBtn.disabled = false;
            downloadPdfBtn.textContent = 'Generate & Download PDF';
          }, 1000);
        } else {
          alert('Error: ' + (data.error || 'Unknown error occurred'));
          downloadPdfBtn.disabled = false;
          downloadPdfBtn.textContent = 'Generate & Download PDF';
        }
      })
      .catch(error => {
        console.error('Error:', error);
        alert('Error generating resume. Please try again.');
        downloadPdfBtn.disabled = false;
        downloadPdfBtn.textContent = 'Generate & Download PDF';
      });
    });
  }
});

