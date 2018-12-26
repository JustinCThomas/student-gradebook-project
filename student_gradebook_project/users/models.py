from django.db import models
from django.contrib.auth.models import User

POSSIBLE_GRADES = (
    ("a", "A"),
    ("b", "B"),
    ("c", "C"),
    ("f", "F"),
    ("not enrolled", "NOT ENROLLED")
)

# Create your models here.
class Student(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
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
