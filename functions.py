import sqlite3
from read_csv import students

gradebook = sqlite3.connect('database.db')
cursor = gradebook.cursor()

# Sets up the four database tables

student_table = """
CREATE TABLE IF NOT EXISTS students (
    id integer PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    Art TEXT,
    Math TEXT,
    History TEXT,
    Literature TEXT,
    Science TEXT
)"""

teacher_table = """
CREATE TABLE IF NOT EXISTS teachers (
    id integer PRIMARY KEY AUTOINCREMENT,
    name TEXT
)"""

student_accounts = """
CREATE TABLE IF NOT EXISTS student_accounts (
    id integer NOT NULL,
    email TEXT unique,
    password TEXT,
    FOREIGN KEY (id) REFERENCES students (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)"""

teacher_accounts = """
CREATE TABLE IF NOT EXISTS teacher_accounts (
    id integer NOT NULL,
    email TEXT unique,
    password TEXT,
    FOREIGN KEY (id) REFERENCES teachers(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)"""


cursor.execute(student_table)
cursor.execute(teacher_table)
cursor.execute(student_accounts)
cursor.execute(teacher_accounts)

gradebook.commit()

# Enters student and teacher information into the database tables

student_classes_template = "INSERT OR IGNORE INTO students (name, Art, Math, History, Literature, Science) VALUES (?, ?, ?, ?, ?, ?)"

for key, value in students.items():
    cursor.execute(student_classes_template, (key, value['subjects']['Art'], value['subjects']['Math'], value['subjects']['History'], value['subjects']['Literature'], value['subjects']['Science']))


teachers_template = "INSERT OR IGNORE INTO teachers (name) VALUES (?)"
teachers_list = ['Astro', 'Brian', 'Hilbert', 'Jermaine', 'Justin', 'Matilda', 'Sharon' ]

for i in teachers_list:
    print(i)
    cursor.execute(teachers_template, (i,))


student_account_template = "INSERT INTO student_accounts (id, email, password) VALUES (?, ?, ?)"
stu_id_num = 1
for key, value in students.items():
    cursor.execute(student_account_template, (str(stu_id_num), "student%s@gmail.com" % str(stu_id_num), "password%s" % str(stu_id_num)))
    stu_id_num += 1

teacher_account_template = "INSERT INTO teacher_accounts (id, email, password) VALUES (?, ?, ?)"
teacher_id_num = 1
for i in range(1, 8):
    cursor.execute(teacher_account_template, (teacher_id_num, "%s@tkh.org" % teachers_list[i - 1].lower(), "admin%s" % i))
    teacher_id_num += 1

gradebook.commit()
gradebook.close()

## search each object

# for i in search_features:
#     if i == inputType:
#         searchType = i
#         break
#
#
# for i in objects:
#     if i.searchType == input:
#         return i
