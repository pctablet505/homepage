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
    print('\n'*5)
    print(photos)
    print('\n'*5)
    return render_template('home.html', routes=routes, os=os, photos=photos, path=path)


@app.route('/contact')
def contact():

    contacts = {
        'Mail': ('pctablet505@gmail.com', 'mailto:pctablet505@gmail.com'),
        'Phone': ('+91 8709253658', 'tel:+91 8709253658'),
        'LinkedIn': ('@pctablet505', 'https://www.linkedin.com/in/pctablet505'),
        'Hackerrank': ('@pctablet505', 'https://www.hackerrank.com/pctablet505'),
        'GitHub': ('@pctablet505', 'https://www.github.com/pctablet505'),
        'Instagram': ('pctablet505', 'https://www.instagram.com/pctablet505')
    }
    return render_template('contact.html', routes=routes, contacts=contacts)


@app.route('/certifications')
def certifications():

    certificates = [
        {'credential': 'https://www.hackerrank.com/certificates/58d066424a1e',
         'src': 'static/certificates/C Advanced.png',
         'title': 'C Advanced'},
        {'credential': 'https://www.hackerrank.com/certificates/0c61249bbe1d',
            'src': 'static/certificates/C Basic.png',
            'title': 'C Basic'},
        {'credential': 'https://www.hackerrank.com/certificates/337182b9dc84',
            'src': 'static/certificates/C Intermediate.png',
            'title': 'C Intermediate'},
        {'credential': 'https://cs50.harvard.edu/certificates/2b1773c1-473d-4a7b-89ae-460d23154126',
            'src': 'static/certificates/CS50 AI.png',
            'title': 'CS50 AI'},
        {'credential': 'https://www.hackerrank.com/certificates/92d056e955d2',
            'src': 'static/certificates/CSS.png',
            'title': 'CSS'},
        {'credential': 'https://www.hackerrank.com/certificates/253bacd0f0c0',
            'src': 'static/certificates/Java.png',
            'title': 'Java'},
        {'credential': 'https://www.kaggle.com/learn/certification/pctablet505/intermediate-machine-learning',
            'src': 'static/certificates/Kaggle - Intermediate Machine Learning.png',
            'title': 'Kaggle Intermediate Machine Learning'},
        {'credential': 'https://www.kaggle.com/learn/certification/pctablet505/intro-to-deep-learning',
            'src': 'static/certificates/Kaggle - Intro to Deep Learning.png',
            'title': 'Kaggle Intro to Deep Learning'},
        {'credential': 'https://www.kaggle.com/learn/certification/pctablet505/intro-to-machine-learning',
            'src': 'static/certificates/Kaggle - Intro to Machine Learning.png',
            'title': 'Kaggle Intro to Machine Learning'},
        {'credential': 'https://www.hackerrank.com/certificates/fc7b9af8aac8',
            'src': 'static/certificates/problem Solving Advanced.png',
            'title': 'Problem Solving Advanced'},
        {'credential': 'https://www.hackerrank.com/certificates/e3c6568f71c6',
            'src': 'static/certificates/Problem Solving Basic.png',
            'title': 'Problem Solving Basic'},
        {'credential': 'https://www.hackerrank.com/certificates/f5bcd6aa9355',
            'src': 'static/certificates/Problem Solving Intermediate.png',
            'title': 'Problem Solving Intermediate'},
        {'credential': 'https://www.hackerrank.com/certificates/6e9c190da189',
            'src': 'static/certificates/Python Advanced.png',
            'title': 'Python Advanced'},
        {'credential': 'https://www.hackerrank.com/certificates/93d10484c124',
            'src': 'static/certificates/Python Basic.png',
            'title': 'Python Basic'},
        {'credential': 'https://www.hackerrank.com/certificates/9ecfb2a355a2',
            'src': 'static/certificates/Python Intermediate.png',
            'title': 'Python Intermediate'},
        {'credential': 'https://www.hackerrank.com/certificates/2508bf1f2b12',
            'src': 'static/certificates/SQL Basic.png',
            'title': 'SQL Basic'},
        {'credential': 'http://ude.my/UC-d7c52c49-464f-4b63-a9b4-2da5d4c53ff4/',
            'src': 'static/certificates/Machine Learning.jpg',
            'title': 'Udemy Complete 2020 Data Science & Machine Learning Bootcamp'},
        {'credential': 'https://www.udemy.com/certificate/UC-37c2faaf-17c4-4089-ab2d-18190a8aa61f/',
            'src': 'static/certificates/DSA.jpg',
            'title': 'Udemy Data Structures and Algorithms'},
        {'credential': 'https://www.kaggle.com/learn/certification/pctablet505/intermediate-machine-learning',
            'src': 'static/certificates/Python.jpg',
            'title': 'Udemy Python'},
        {'credential': 'https://www.kaggle.com/learn/certification/pctablet505/python',
            'src': 'static/certificates/Kaggle - Python.png',
            'title': 'kaggle Python'},
        {'credential': 'https://www.hackerrank.com/certificates/74470a9fe364',
            'src': 'static/certificates/SQL Intermediate.png',
            'title': 'SQL Intermediate'},
    ]
    certificates.sort(key=lambda x: x['title'])

    return render_template('certifications.html', routes=routes, certificates=certificates)


@app.route('/home')
def home():
    return redirect('/')


@app.route('/<name>')
def route(name):
    return render_template(f'{name}.html', routes=routes)

