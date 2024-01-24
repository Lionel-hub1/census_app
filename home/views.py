from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    context = {
        "records" : Person.objects.all()
    }
    return render(request, 'index.html', context)
