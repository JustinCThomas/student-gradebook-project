from werkzeug.security import generate_password_hash
from app import app

# from flask_sqlalchemy import SQLAlchemy

# import sys
# if sys.version_info >= (3, 0):
#     enable_search = False
# else:
#     enable_search = True
#     import flask_whooshalchemy as whooshalchemy



# db = SQLAlchemy(app)


# students = {}
# subjects = ["Art", "Math", "History", "Literature", "Science"]
# grades = ["A", "B", "C", "F"]


# class Student(db.Model):
#     __searchable__ = ['username','firstName','lastName']
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     firstName = db.Column(db.String(64), index=True)
#     lastName = db.Column(db.String(64), index=True)
#     scienceGrade = db.Column(db.String(120), index=True)
#     artGrade  = db.Column(db.String(120), index=True)
#     mathGrade  = db.Column(db.String(120), index=True)
#     literatureGrade  = db.Column(db.String(120), index=True)
#     historyGrade  = db.Column(db.String(120), index=True)
#     gpa = db.Column(db.Float(120), index=True)
#     password_hash = db.Column(db.String(128))


#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different username.')


#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)

#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)

#     def __repr__(self):
#         return '<Student {}>'.format(self.username)   

#     if enable_search:
#         whooshalchemy.whoosh_index(app, Student)


# s = Student(username='Samda',firstName = 'same',lastName ='person',scienceGrade ="A",artGrade ="A", mathGrade ="A",
# literatureGrade="A",historyGrade="A",gpa =4.0,password_hash="moose")


