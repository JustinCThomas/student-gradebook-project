from flask import redirect, url_for, render_template, request
import sqlite3
from app import app

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

            return render_template('teacher.html', row = row)
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

@app.route('/process-login')
def process_login():
    pass

@app.route('/student')
def student():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from students where id = 1")

    row = cur.fetchone()

    return render_template('student.html', row = row)

@app.route('/teacher')
def teacher():
    con = sqlite3.connect('database.db')
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute("select * from teachers where id = 1")

    row = cur.fetchone()
    return render_template('teacher.html', row = row)


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
