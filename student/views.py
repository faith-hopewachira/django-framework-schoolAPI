from .forms import StudentRegistrationForm
from django.shortcuts import render, redirect

# Create your views here.
def register_student(request):
    # form = StudentRegistrationForm()
    # #THE REQUEST, THE TEMPLATE, THE DATA BEING RENDERED 
    # return render(request, "student/register_student.html", {"form":form})

    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register_student")

    else:
        form= StudentRegistrationForm()
    # return render()
    return render(request, "student/register_student.html", {"form": form})
