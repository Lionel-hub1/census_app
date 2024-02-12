from django.shortcuts import render, redirect
from .models import *


def home(request):
    """This function returns the home page of the application. It also returns the records of all the people in the database."""
    context = {
        "records": Person.objects.all()
    }
    return render(request, 'index.html', context)


def add(request):
    """This function handles the submission of adding a new person page and form."""
    if request.method == "POST":
        person = Person()
        person.first_name = request.POST["first_name"]
        person.last_name = request.POST["last_name"]
        person.age = request.POST["age"]
        person.occupation = request.POST["occupation"]
        person.location = request.POST["location"]
        person.save()
        return redirect('/')

    return render(request, 'addperson.html')
