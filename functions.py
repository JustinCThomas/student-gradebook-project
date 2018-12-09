import sqlite3
from read_csv import students

gradebook = sqlite3.connect('database.db')
cursor = gradebook.cursor()

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
)
"""

student_accounts = """
CREATE TABLE IF NOT EXISTS student_accounts (
    id integer NOT NULL,
    email TEXT unique,
    password TEXT,
    FOREIGN KEY (id) REFERENCES students (id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)
"""

teacher_accounts = """
CREATE TABLE IF NOT EXISTS teacher_accounts (
    id integer NOT NULL,
    email TEXT unique,
    password TEXT,
    FOREIGN KEY (id) REFERENCES teachers(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)
"""


cursor.execute(student_table)
for key, value in students.items():
    print(key)
    print()


print("\n\n\n")
print(students["MAURICE BEY"])

cursor.execute(teacher_table)


cursor.execute(student_accounts)


cursor.execute(teacher_accounts)




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
