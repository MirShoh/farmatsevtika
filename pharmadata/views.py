from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Faculty
from .forms import FacultyForm

def login_required_decorator(func):
    return login_required(function=func, login_url="login-page")

def login_page(request):
    if request.POST:
        username = request.POST.get("login", None)
        password = request.POST.get("parol", None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main-page")
    return render(request, "login.html")

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login-page")

@login_required_decorator
def index(request):
    return render(request, 'index.html')

def all_faculties(request):
    faculties = Faculty.objects.all()
    ctx = {
        'faculties': faculties,
    }
    return render(request, 'all-faculty.html', ctx)

@login_required_decorator
def add_faculty(request):
    form = FacultyForm(request.POST or None)
    if request.POST and form.is_valid():
        form.save()
    return render(request, 'add-faculty.html')

@login_required_decorator
def faculty_edit(request, pk):
    model = Faculty.objects.get(pk=pk)
    form = FacultyForm(request.POST or None, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("all-faculties")
    ctx = {
        "model": model,
        "form": form,
    }
    return render(request, "edit-faculty.html", ctx)

@login_required_decorator
def faculty_delete(request, pk):
    model = Faculty.objects.get(pk=pk)
    model.delete()
    return redirect("all-faculties")

@login_required_decorator
def add_user(request):
    return render(request, 'add-user.html')

