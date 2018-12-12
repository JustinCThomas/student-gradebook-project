from flask import render_template, request
import sqlite3
from app import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

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
