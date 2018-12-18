import sqlite3
# Import the students dictionary from read_csv
from read_csv import students

# Accesses or creates the "database.db" file
# Establishes a connection with 'database.db'
gradebook = sqlite3.connect('database.db')
# Creates a cursor object for later executing SQL commands
cursor = gradebook.cursor()

# Sets up the four database tables

# Contains the sqlite3 code for creating the students table
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

# Contains the sqlite3 code for creating the teachers table
teacher_table = """
CREATE TABLE IF NOT EXISTS teachers (
    id integer PRIMARY KEY AUTOINCREMENT,
    name TEXT
)"""

# Contains the sqlite3 code for creating the student_accounts table
student_accounts = """
CREATE TABLE IF NOT EXISTS student_accounts (
    id integer NOT NULL,
    email TEXT unique,
    password TEXT,
    FOREIGN KEY (id) REFERENCES students (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)"""

# Contains the sqlite3 code for creating the teacher_accounts table
teacher_accounts = """
CREATE TABLE IF NOT EXISTS teacher_accounts (
    id integer NOT NULL,
    email TEXT unique,
    password TEXT,
    FOREIGN KEY (id) REFERENCES teachers(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)"""

# Executes the code and Creates the tables
cursor.execute(student_table)
cursor.execute(teacher_table)
cursor.execute(student_accounts)
cursor.execute(teacher_accounts)

# Commits the changes to the database, so that further code snippets that depend on the
# tables existing in the database work properly
gradebook.commit()



# Enters student and teacher information into the database tables

# Adds students from the students dictionary to the students table in the database
student_classes_template = "INSERT OR IGNORE INTO students (name, Art, Math, History, Literature, Science) VALUES (?, ?, ?, ?, ?, ?)"

for key, value in students.items():
    cursor.execute(student_classes_template, (key, value['subjects']['Art'], value['subjects']['Math'], value['subjects']['History'], value['subjects']['Literature'], value['subjects']['Science']))

# Creates and adds teacher entries to the teachers table
teachers_template = "INSERT OR IGNORE INTO teachers (name) VALUES (?)"
teachers_list = ['Astro', 'Brian', 'Hilbert', 'Jermaine', 'Justin', 'Matilda', 'Sharon' ]

for i in teachers_list:
    print(i)
    cursor.execute(teachers_template, (i,))


# Creates student account information to then add to a database
# emails follow the model of "student1@gmail.com" and passwords follow the model of "password1"
# where 1 is the student's id number
student_account_template = "INSERT INTO student_accounts (id, email, password) VALUES (?, ?, ?)"
stu_id_num = 1
for key, value in students.items():
    cursor.execute(student_account_template, (str(stu_id_num), "student%s@gmail.com" % str(stu_id_num), "password%s" % str(stu_id_num)))
    stu_id_num += 1

# Creates teacher account information to then add to a database
# emails have "@tkh.org" extensions and passwords all start with "admin"
teacher_account_template = "INSERT INTO teacher_accounts (id, email, password) VALUES (?, ?, ?)"
teacher_id_num = 1
for i in range(1, 8):
    cursor.execute(teacher_account_template, (teacher_id_num, "%s@tkh.org" % teachers_list[i - 1].lower(), "admin%s" % i))
    teacher_id_num += 1

# Commit the latest changes to the database
gradebook.commit()
# Close the database conection
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
