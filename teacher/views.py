from django.shortcuts import render
from .forms import TeacherRegistrationForm

# Create your views here.
def register_teacher(request):
    form = TeacherRegistrationForm()
    #THE REQUEST, WHERE YOU ARE RENDERING, THE DATA BEING RENDERED 
    return render(request, "teacher/register_teacher.html", {"form":form})