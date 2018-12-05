from flask import Flask
from flask import render_template

app = Flask(__name__)

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
