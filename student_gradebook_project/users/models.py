from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    Art = models.CharField(max_length=100)
    Math = models.CharField(max_length=100)
    History = models.CharField(max_length=100)
    Literature = models.CharField(max_length=100)
    Science= models.CharField(max_length=100)

    def __str__(self):
        return f'Student: {self.user.username}'


class Teacher(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Teacher: {self.user.username}'
