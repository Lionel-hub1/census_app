from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    context = {
        "records" : Person.objects.all()
    }
    return render(request, 'index.html', context)


def add(request):
    if request.method == "POST":
        person = Person()
        person.first_name = request.POST["first_name"]
        person.last_name = request.POST["last_name"]
        person.age = request.POST["age"]
        person.occupation = request.POST["occupation"]
        person.location = request.POST["location"]
        person.save()

    return render(request, 'addperson.html')
