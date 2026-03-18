# Portfolio Website with Flask Backend

A modern portfolio website built with Flask backend featuring skill-based resume generation.

## Features

- **Portfolio Display**: Showcase your education, skills, projects, and accomplishments
- **Resume Builder**: Select specific skills to generate a customized PDF resume
- **Contact Form**: Integrated contact form with Flask backend
- **Dark Mode**: Toggle between light and dark themes
- **Responsive Design**: Works on all devices

## Installation

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up the project structure:**
   - The project already has the correct structure:
     - `app.py` - Flask application
     - `templates/` - HTML templates
     - `static/` - CSS, JavaScript, and images
     - `resumes/` - Generated PDF resumes (created automatically)

3. **Move your images:**
   - If you have an `images/` folder, move it to `static/images/`
   - Update the image path in `templates/index.html` if needed

## Running the Application

1. **Start the Flask server:**
   ```bash
   python app.py
   ```

2. **Open your browser:**
   - Navigate to `http://localhost:5000`
   - The portfolio website will be displayed

## Usage

### Resume Builder

1. Navigate to the "Resume Builder" section
2. Select the skills you want to include in your resume
3. Click "Select All" or "Deselect All" for quick selection
4. Click "Generate Resume PDF" to create and download your customized resume

### API Endpoints

- `GET /` - Main portfolio page
- `GET /api/skills` - Get all available skills
- `POST /api/generate-resume` - Generate resume PDF (requires JSON: `{"skills": ["skill1", "skill2", ...]}`)
- `GET /api/download-resume/<filename>` - Download generated resume
- `POST /api/contact` - Submit contact form (requires JSON: `{"name": "...", "email": "...", "message": "..."}`)

## Project Structure

```
portfolio/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── style.css         # Stylesheet
│   ├── script.js         # JavaScript
│   └── images/           # Image assets
└── resumes/              # Generated PDFs (auto-created)
```

## Customization

### Update Portfolio Data

Edit the `PORTFOLIO_DATA` dictionary in `app.py` to update:
- Personal information
- Education details
- Skills
- Projects
- Accomplishments

### Styling

Modify `static/style.css` to change the appearance of your portfolio.

## Requirements

- Python 3.7+
- Flask 3.0.0
- flask-cors 4.0.0
- reportlab 4.0.7 (for PDF generation)
- Pillow 10.1.0 (for image processing)

## Notes

- Generated resumes are stored in the `resumes/` directory
- The contact form currently logs submissions (you can extend it to send emails)
- Make sure to update contact information in `app.py` before deploying

## License

© 2025 Your Name. All rights reserved.
