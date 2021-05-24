import os
from flask import Flask, render_template, redirect

app = Flask(__name__)

files = os.listdir(path='./templates')
routes = []
for x in files:
    if len(x) >= 5 and x[-5:] == '.html':
        if x != 'layout.html':
            routes.append(x[:-5])


@app.route('/')
def index():
    path = ('./static/me')
    photos = os.listdir(path=path)
    print('\n' * 5)
    print(photos)
    print('\n' * 5)
    return render_template('home.html', routes=routes, os=os, photos=photos, path=path)


@app.route('/contact')
def contact():
    contacts = {
        'Mail': ('pctablet505@gmail.com', 'mailto:pctablet505@gmail.com'),
        'Phone': ('+91 8709253658', 'tel:+91 8709253658'),
        'LinkedIn': ('@pctablet505', 'https://www.linkedin.com/in/pctablet505'),
        'Hackerrank': ('@pctablet505', 'https://www.hackerrank.com/pctablet505'),
        'GitHub': ('@pctablet505', 'https://www.github.com/pctablet505'),
        'Instagram': ('pctablet505', 'https://www.instagram.com/pctablet505'),
    }
    return render_template('contact.html', routes=routes, contacts=contacts)


@app.route('/certifications')
def certifications():
    from certificates import certificates
    certificates.sort(key=lambda x: x.title)

    return render_template('certifications.html', routes=routes, certificates=certificates)


@app.route('/projects')
def projects():
    from projects_list import projects_list

    return render_template('projects.html', routes=routes, projects=projects_list)


@app.route('/home')
def home():
    return redirect('/')


@app.route('/<name>')
def route(name):
    return render_template(f'{name}.html', routes=routes)
