from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Teacher
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created! You can now log in!')
            return redirect('login')

    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

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
