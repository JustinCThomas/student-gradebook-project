from flask import render_template
from app import app

@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')
