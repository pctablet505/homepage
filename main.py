import os
from flask import Flask, render_template, redirect
from certificates import certificates
from projects_list import projects_list
from skills import skills
from contacts import contacts
from achievements import achievements as achievements_list
import resume1page as r1
from education import education as edu

app = Flask(__name__)

files = os.listdir(path='./templates')
routes = []
for x in files:
    if len(x) >= 5 and x[-5:] == '.html':
        if x not in ['layout.html','layout_resume.html']:
            routes.append(x[:-5])
routes.sort()


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
    return render_template('contact.html', routes=routes, contacts=contacts)


@app.route('/certifications')
def certifications():
    return render_template('certifications.html', routes=routes, certificates=certificates)


@app.route('/projects')
def projects():
    return render_template('projects.html', routes=routes, projects=projects_list)


@app.route('/home')
def home():
    return redirect('/')


@app.route('/achievements')
def achievements():
    return render_template('achievements.html', routes=routes, achievements=achievements_list)


@app.route('/<name>')
def route(name):
    return render_template(f'{name}.html', routes=routes)


@app.route('/resume')
def resume():
    hobbies = ['Digital Arts', 'Tabla Playing']
    return render_template('resume.html', routes=routes, skills=skills, projects=projects_list, contacts=contacts,
                           achievements=achievements_list, hobbies=hobbies, certificates=certificates)


@app.route('/resume1page')
def resume1page():
    hobbies = ['Digital Arts', 'Tabla Playing', 'Gaming',]
    print(routes)
    return render_template('resume1page.html',  skills=r1.skills, projects=projects_list, contacts=r1.contacts,
                           achievements=achievements_list, hobbies=hobbies, certificates=r1.certificates,education=edu)

if __name__=='__main__':
    app.run(debug=True)