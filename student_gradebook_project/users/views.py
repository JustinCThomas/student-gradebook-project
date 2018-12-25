from django.shortcuts import render
from .models import Student, Teacher

# Create your views here.
def student(request):
    context = {
        'student': Student
    }

    return render(request, 'users/student.html', context)

def teacher(request):
    context = {
        'students': Student.objects.all(),
        'teacher': Teacher
    }

    return render(request, 'users/teacher.html', context)
