from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('student/', views.student, name='users-student'),
    path('teacher/', views.teacher, name='users-teacher')
]
