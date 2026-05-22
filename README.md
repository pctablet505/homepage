# Homepage

A dynamic personal portfolio built with **Flask**.

## Description

This is a server-rendered personal homepage and portfolio application that showcases projects, skills, achievements, certifications, education, experience, and contact information. It serves as a dynamic alternative to the static GitHub Pages portfolio ([pctablet505.github.io](https://pctablet505.github.io)), with content driven by Python data modules.

## Tech Stack

- **Backend**: Flask (Python)
- **Server**: Gunicorn
- **Frontend**: HTML5, CSS3, JavaScript
- **Templates**: Jinja2 (Flask templating engine)
- **Deployment**: Heroku-ready (`Procfile`); Google App Engine (`app.yaml`)

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/pctablet505/homepage.git
   cd homepage
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application locally**
   ```bash
   python main.py
   ```
   Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

   Alternatively, using Gunicorn:
   ```bash
   gunicorn wsgi:app
   ```

## Project Structure

```
homepage/
├── main.py                 # Flask application entry point
├── wsgi.py                 # WSGI entry point for Gunicorn
├── application.py          # Alternative application entry (legacy/alias)
├── Procfile                # Heroku deployment config
├── app.yaml                # Google App Engine config
├── requirements.txt        # Python dependencies
├── static/                 # CSS, JS, images, resume files
│   ├── css/
│   ├── js/
│   └── me/                 # Photos
├── templates/              # Jinja2 HTML templates
│   ├── home.html
│   ├── about.html
│   ├── projects.html
│   ├── certifications.html
│   ├── achievements.html
│   ├── skills.html
│   ├── education.html
│   ├── experience.html
│   ├── contact.html
│   ├── resume.html
│   ├── layout.html
│   └── layout_resume.html
├── projects_list.py        # Projects data
├── skills.py               # Skills data
├── achievements.py         # Achievements data
├── certificates.py         # Certifications data
├── education.py            # Education data
├── experience.py           # Work experience data
├── contacts.py             # Contact information
├── resume1page.py          # Resume content
└── .gcloudignore           # GCloud ignore rules
```

## Deployment Notes

- **Heroku**: The `Procfile` is configured with `web: gunicorn wsgi:app`. Push to a Heroku remote to deploy.
- **Google App Engine**: `app.yaml` is included for GAE standard environment deployment.
