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

    if request.method == 'POST':
        error = None

        con = sqlite3.connect('database.db')
        con.row_factory = sqlite3.Row

        account = "teacher_accounts" if request.form['username'][-7:] == "tkh.org" else "student_accounts"

        cur = con.cursor()
        cur.execute("select * from {0} where email = '{1}' and password = '{2}'".format(account, request.form['username'], request.form['password']))

        row = cur.fetchone()
        if row and account == "teacher_accounts":
            cur.execute("select * from teachers where id = {0}".
            format(row['id']))

            row = cur.fetchone()

            cur.execute("select * from students")
            data = cur.fetchall()

            return render_template('TeachersHomePage.html', row = row, data = data)
            # return redirect(url_for('teacher'), row)
        elif row and account == "student_accounts":
            cur.execute("select * from students where id = {0}".
            format(row['id']))

            row = cur.fetchone()

            return render_template('student.html', row = row)
        else:
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
            # return redirect(url_for('student'))
        # else:
        #     return redirect(url_for('teacher'))

    return render_template('login.html')

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
    searchUser(cur,request.form['username'])
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
        print ('No such user')
    else:
        print (the_username, 'has the id', user['user_id'])
        render_template('TeachersHomePage.html')
