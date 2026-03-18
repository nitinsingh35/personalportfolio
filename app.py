from flask import Flask, render_template, request, jsonify, send_file
from flask_cors import CORS
import json
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from io import BytesIO

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['UPLOAD_FOLDER'] = 'resumes'

# Ensure resumes directory exists
os.makedirs('resumes', exist_ok=True)

# Portfolio data structure
PORTFOLIO_DATA = {
    "name": "Nitin Kumar Singh",
    "title": "Full Stack Web Developer & Future Tech Entrepreneur",
    "about": "I'm a passionate B.Tech CSE student from Jharkhand, building modern web applications and learning every day. My goal is to create meaningful software and someday run my own company.",
    "email": "your.email@example.com",
    "phone": "+91-XXXXXXXXXX",
    "location": "Jharkhand, India",
    "linkedin": "https://www.linkedin.com/in/nitin-kumar-singh-/",
    "github": "https://github.com/nitin62043",
    "education": [
        {
            "degree": "B.Tech CSE",
            "institution": "Lovely Professional University, Punjab",
            "period": "2023-Present",
            "details": "Bachelor of Technology (B.Tech) in Computer Science & Engineering"
        },
        {
            "degree": "Higher Secondary",
            "institution": "Govt Inter College, Daltonganj",
            "period": "2020-2022",
            "details": "Scored: 74.4% in Board Exams"
        },
        {
            "degree": "Secondary",
            "institution": "Swami Vivekanand School",
            "period": "Passed in 2020",
            "details": "Scored: 84.4% in Board Exams"
        }
    ],
    "skills": {
        "programming": ["Python", "Java", "C", "C++"],
        "web": ["HTML", "CSS", "JavaScript", "PHP"],
        "database": ["MySQL", "MongoDB"],
        "tools": ["MS Excel", "Google Sheets", "Git", "GitHub", "VS Code", "ChatGPT", "Google Colab"],
        "soft_skills": ["Problem-Solving", "Time Management", "Teamwork", "Communication"]
    },
    "projects": [
        {
            "name": "EcoRecycle",
            "description": "Helps users find e-waste centers & learn about safe recycling.",
            "link": "https://github.com/nitin62043/EcoRecycle-"
        },
        {
            "name": "Virtual Memory Optimization Challenges",
            "description": "A series of challenges focused on optimizing virtual memory usage in applications.",
            "link": "https://github.com/nitin62043/Virtual-Memory-Optimization-Challenge"
        },
        {
            "name": "ChatBot For App Suggestion",
            "description": "A chatbot that suggests applications based on user preferences and requirements.",
            "link": "https://github.com/nitin62043/chatbot-for-app-suggestion"
        }
    ],
    "accomplishments": [
        "Java, C, C++, DSA - Neo Colab Certificates",
        "Networking and System Certifications",
        "Full Stack Web Development Certification",
        "Code-A-Haunt Hackathon Participant"
    ],
    "social_work": "Volunteer For 2 Month at PanchGavya And Ayurvedic Anusandhan Kendra, Working On Tree Plantation And Caring Of Animals."
}

def generate_resume_pdf(selected_skills, output_path):
    """Generate a professional PDF resume based on selected skills"""
    doc = SimpleDocTemplate(output_path, pagesize=A4,
                            rightMargin=0.5*inch, leftMargin=0.5*inch,
                            topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    elements = []
    styles = getSampleStyleSheet()
    
    # Define custom styles
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontSize=18,
        textColor=colors.HexColor('#000000'),
        spaceAfter=4,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold'
    )
    
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#333333'),
        spaceAfter=2,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )
    
    section_heading_style = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#000000'),
        spaceAfter=6,
        spaceBefore=8,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold',
        borderPadding=3
    )
    
    entry_title_style = ParagraphStyle(
        'EntryTitle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#000000'),
        spaceAfter=2,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold'
    )
    
    entry_subtitle_style = ParagraphStyle(
        'EntrySubtitle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#444444'),
        spaceAfter=1,
        alignment=TA_LEFT,
        fontName='Helvetica-Oblique'
    )
    
    entry_detail_style = ParagraphStyle(
        'EntryDetail',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#333333'),
        spaceAfter=2,
        leftIndent=0.2*inch,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )
    
    normal_style = ParagraphStyle(
        'Normal9',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#333333'),
        spaceAfter=3,
        alignment=TA_LEFT,
        fontName='Helvetica',
        leading=11
    )
    
    # Header: Name and Contact Information
    elements.append(Paragraph(PORTFOLIO_DATA['name'], name_style))
    
    linkedin_url = PORTFOLIO_DATA.get('linkedin', '')
    github_url = PORTFOLIO_DATA.get('github', '')
    
    contact_lines = [
        f"<b>LinkedIn:</b> <font color='blue'><u>{linkedin_url.split('/')[-2] if linkedin_url else 'LinkedIn'}</u></font>",
        f"<b>Email:</b> {PORTFOLIO_DATA.get('email', 'your.email@example.com')}",
        f"<b>Mobile:</b> {PORTFOLIO_DATA.get('phone', '+91-XXXXXXXXXX')}"
    ]
    
    for contact in contact_lines:
        elements.append(Paragraph(contact, contact_style))
    
    elements.append(Spacer(1, 0.15*inch))
    
    # Add horizontal line
    from reportlab.platypus import HRFlowable
    hr = HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cccccc'))
    elements.append(hr)
    elements.append(Spacer(1, 0.1*inch))
    
    # About Section
    if PORTFOLIO_DATA.get('about'):
        elements.append(Paragraph("PROFESSIONAL SUMMARY", section_heading_style))
        elements.append(Paragraph(PORTFOLIO_DATA['about'], normal_style))
        elements.append(Spacer(1, 0.08*inch))
    
    # Education Section
    if PORTFOLIO_DATA.get('education'):
        elements.append(Paragraph("EDUCATION", section_heading_style))
        for edu in PORTFOLIO_DATA['education']:
            elements.append(Paragraph(f"<b>{edu['degree']}</b>", entry_title_style))
            elements.append(Paragraph(f"{edu['institution']} | {edu['period']}", entry_subtitle_style))
            if edu.get('details'):
                elements.append(Paragraph(edu['details'], entry_detail_style))
            elements.append(Spacer(1, 0.06*inch))
        elements.append(Spacer(1, 0.05*inch))
    
    # Skills Section (filtered by selected skills)
    if selected_skills:
        elements.append(Paragraph("TECHNICAL SKILLS", section_heading_style))
        
        skill_categories = {
            "Programming Languages": [],
            "Web Development": [],
            "Database": [],
            "Tools & Platforms": [],
            "Soft Skills": []
        }
        
        all_skills = {
            "Programming Languages": PORTFOLIO_DATA['skills']['programming'],
            "Web Development": PORTFOLIO_DATA['skills']['web'],
            "Database": PORTFOLIO_DATA['skills']['database'],
            "Tools & Platforms": PORTFOLIO_DATA['skills']['tools'],
            "Soft Skills": PORTFOLIO_DATA['skills']['soft_skills']
        }
        
        for category, skills_list in all_skills.items():
            filtered_skills = [skill for skill in skills_list if skill in selected_skills]
            if filtered_skills:
                skill_categories[category] = filtered_skills
        
        for category, skills_list in skill_categories.items():
            if skills_list:
                category_text = f"<b>{category}:</b> {', '.join(skills_list)}"
                elements.append(Paragraph(category_text, normal_style))
        
        elements.append(Spacer(1, 0.08*inch))
    
    # Projects Section
    if PORTFOLIO_DATA.get('projects'):
        elements.append(Paragraph("PROJECTS", section_heading_style))
        for project in PORTFOLIO_DATA['projects']:
            elements.append(Paragraph(f"<b>{project['name']}</b>", entry_title_style))
            elements.append(Paragraph(project['description'], entry_detail_style))
            if project.get('link'):
                elements.append(Paragraph(f"<font color='blue'><u>{project['link']}</u></font>", entry_detail_style))
            elements.append(Spacer(1, 0.05*inch))
        elements.append(Spacer(1, 0.05*inch))
    
    # Training & Certifications Section
    if PORTFOLIO_DATA.get('accomplishments'):
        elements.append(Paragraph("TRAINING & CERTIFICATIONS", section_heading_style))
        for acc in PORTFOLIO_DATA['accomplishments']:
            elements.append(Paragraph(f"• {acc}", entry_detail_style))
        elements.append(Spacer(1, 0.05*inch))
    
    # Social Work Section
    if PORTFOLIO_DATA.get('social_work'):
        elements.append(Paragraph("SOCIAL WORK & VOLUNTEERING", section_heading_style))
        elements.append(Paragraph(PORTFOLIO_DATA['social_work'], normal_style))
    
    # Build PDF
    doc.build(elements)

@app.route('/')
def index():
    """Render the main portfolio page"""
    return render_template('index.html', portfolio_data=PORTFOLIO_DATA)

@app.route('/api/skills', methods=['GET'])
def get_skills():
    """Get all available skills"""
    return jsonify({
        "success": True,
        "skills": PORTFOLIO_DATA['skills']
    })

@app.route('/api/generate-resume', methods=['POST'])
def generate_resume():
    """Generate resume PDF based on selected skills"""
    try:
        data = request.get_json()
        selected_skills = data.get('skills', [])
        
        if not selected_skills:
            return jsonify({
                "success": False,
                "error": "No skills selected"
            }), 400
        
        # Generate unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"resume_{timestamp}.pdf"
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        # Generate PDF
        generate_resume_pdf(selected_skills, filepath)
        
        return jsonify({
            "success": True,
            "filename": filename,
            "message": "Resume generated successfully"
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/download-resume/<filename>', methods=['GET'])
def download_resume(filename):
    """Download the generated resume"""
    try:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True, download_name=filename)
        else:
            return jsonify({
                "success": False,
                "error": "File not found"
            }), 404
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submission"""
    try:
        data = request.get_json()
        name = data.get('name', '')
        email = data.get('email', '')
        message = data.get('message', '')
        
        # Here you can add email sending logic or save to database
        # For now, just return success
        
        return jsonify({
            "success": True,
            "message": "Thank you! Your message has been sent."
        })
    
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
