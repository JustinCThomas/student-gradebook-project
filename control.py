from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello  Everyone!"

@app.route('/login')
def login():
    return "Insert Login Page here: "

@app.route('/homepage')
def homepage():
    return "Insert Home Page here: "
