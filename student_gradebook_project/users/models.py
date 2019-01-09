from django.db import models
from django.contrib.auth.models import User

POSSIBLE_GRADES = (
    ("a", "A"),
    ("b", "B"),
    ("c", "C"),
    ("f", "F"),
    ("not enrolled", "NOT ENROLLED")
)

POSSIBLE_RACES = (
    ("black", "Black or African American"),
    ("asian", "Asian"),
    ("latinx", "Latinx"),
    ("white", "White"),
    ("amerindian", "American Indian or Alaska Native"),
    ("hawaiian or pacific islander", "Native Hawaiian or Other Pacific Islander"),
    ("mixed race", "Mixed Race")
)

POSSIBLE_SEX = (
    ("male", "Male"),
    ("female", "Female"),
    ("prefer not to answer", "Prefer Not to Answer")
)

POSSIBLE_GENDER = (
    ("prefer not to answer", "Prefer Not to Answer"),
    ("non-binary", "Non-binary/Gender Non-Conforming/Genderqueer"),
    ("male", "Male"),
    ("female", "Female")
)

POSSIBLE_IEP_504_PLAN = (
    ("iep and 504 plan", "IEP and 504 Plan"),
    ("none", "None"),
    ("iep", "IEP"),
    ("504", "504 Plan")
)


# Create your models here.
class Student(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    Sex = models.CharField(max_length=12, choices=POSSIBLE_SEX, default='')
    Gender = models.CharField(max_length=100, choices=POSSIBLE_GENDER, default='')
    Race = models.CharField(max_length=100, choices=POSSIBLE_RACES, default='')
    IEP_or_504_Plan = models.CharField(max_length=100, choices=POSSIBLE_IEP_504_PLAN, default='None')
    Art = models.CharField(max_length=12, choices=POSSIBLE_GRADES, default='not enrolled')
    Math = models.CharField(max_length=12, choices=POSSIBLE_GRADES, default='not enrolled')
    History = models.CharField(max_length=12, choices=POSSIBLE_GRADES, default='not enrolled')
    Literature = models.CharField(max_length=12, choices=POSSIBLE_GRADES, default='not enrolled')
    Science= models.CharField(max_length=12, choices=POSSIBLE_GRADES, default='not enrolled')

    def __str__(self):
        return f'Student: {self.name}'


class Teacher(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Teacher: {self.name}'
