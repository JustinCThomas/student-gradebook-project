from flask import redirect, url_for, render_template, request
from werkzeug.security import generate_password_hash
import sqlite3

from app import app, models



def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


# from models import Student

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':



        # user = Student.query.filter_by(username=request.form['username']).first()
        # if user is None or not user.check_password(request.form['password'] ):
        #     error = 'Invalid Credentials. Please try again.'


        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
           
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('teacher'))
    return render_template('login.html', error=error)

@app.route('/student')
def student():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from students where id = 1")

    row = cur.fetchone()


    # if request.form['firstName'] or request.form['lastName']:



    return render_template('StudentPage.html', row = row)

@app.route('/teacher')
def teacher():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from teachers where id = 1")

    row = cur.fetchone()
    return render_template('TeachersHomePage.html', row = row)


@app.route('/teacher')
def display_search_results():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from students where id = 1")

    return render_template('TeachersHomePage.html', row = row)


# def valid_login(username,attemptedPassword):
#     hash = generate_password_hash(attemptedPassword)
#     if check_password_hash(username.Student.password_hash,attemptedPassword):
#         redirect(url_for('teacher'))
    
        
    
# def validate_username(self, username):
#         user = Student.query.filter_by(username=username.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different username.')


# def checkUserType(username):
#     if username in teacherList:
#         return redirect(url_for('teacher'))
#     else:
#         return redirect(url_for('student'))

def searchUser(DATABASE, input):
    user = query_db('select * from users where username = ?',
                [input], one=True)
    if user is None:
        print 'No such user'
    else:
        print the_username, 'has the id', user['user_id']
        render_template('TeachersHomePage.html')
