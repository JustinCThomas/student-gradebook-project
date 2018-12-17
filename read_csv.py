import csv
import random
import json

# Initialize the student dictionary that will eventually be exported
# The subjects and grades lists will be used in randomly assigning students classes and grades
students = {}
subjects = ["Art", "Math", "History", "Literature", "Science"]
grades = ["A", "B", "C", "F"]

# Opens the names.txt file for reading
with open("names.txt") as csv_file:
    # Separates the file contents line by line with a comma "," using the csv module
    # Each line is then added as a list to a csv.reader object
    # csv_reader is assigned to this object
    csv_reader = csv.reader(csv_file, delimiter=",")
    for row in csv_reader:
        # These 3 lines initialize the student with a dictionary (dict1)
        # The dictionary (dict1) has a key of "subjects" which holds another dictionary (dict2)
        # dict2 is assigned the five subjects as keys and "Not Enrolled" as values
        # The row is a list of a single string (The student's name),
        # so it must be accessed through indexing as "row[0]"
        students[row[0]] = {"subjects": {}}
        for i in range(5):
            students[row[0]]["subjects"][subjects[i]] = "Not Enrolled"

        # This line is to ensure that each student will be enrolled in at least 1 class
        # That class is chosen at random
        students[row[0]]["subjects"][random.choice(subjects)] = random.choice(grades)

        # This code block will try to assign the student a grade for a class if not already enrolled
        # The subject and grade are chosen at random
        for i in range(4):
            r_choice = random.choice(subjects)
            if students[row[0]]["subjects"][r_choice] == "Not Enrolled":
                students[row[0]]["subjects"][r_choice] = random.choice(grades)

# Outputs dictionary as a json object and then writes it to a .json file
js = json.dumps(students)

with open("students.json", 'w') as json_file:
    json_file.write(js)

# Received help from this source:
# https://stackoverflow.com/questions/29400631/python-writing-nested-dictionary-to-csv
fields = ["Name", "Art", "Math", "History", "Literature", "Science"]

# Outputs dictionary as a .csv file
with open("students.csv", 'w') as stu_csv:
    dict_writer = csv.DictWriter(stu_csv, fields)
    dict_writer.writeheader()
    for i in students:
        dict_writer.writerow({field: students[i]["subjects"].get(field) or i for field in fields})
