from flask import render_template,url_for,redirect
from flask import request
import sqlite3
from app import app

@app.route('/', methods=['GET', 'POST'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            # a= request.form['username']
            # print(a)
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('teacher'))
    return render_template('login.html', error=error)

# @app.route('/student')
# def student():
#     con = sqlite3.connect('database.db')
#     con.row_factory = sqlite3.Row

#     cur = con.cursor()
#     cur.execute("select * from students where id = 1")

#     row = cur.fetchone()

#     return render_template('student.html', row = row)

# @app.route('/teacher')
# def teacher():
#     con = sqlite3.connect('database.db')
#     con.row_factory = sqlite3.Row

#     cur = con.cursor()
#     cur.execute("select * from teachers where id = 1")

#     row = cur.fetchone()
#     return render_template('teacher.html', row = row)




def valid_login(username,password):
    if username in database and password in passDatabase:
        return True
    else:
        return False


def log_the_user_in(username):
    if username in teacherList:
        return redirect(url_for('teacher'))
    else:
        return redirect(url_for('student'))
