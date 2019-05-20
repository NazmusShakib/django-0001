from django.shortcuts import render
from django.views.generic import CreateView
from .models import Person
from django.shortcuts import render


# Create your views here.


def hello_world(request):
    return render(request, 'hello_world.html', {})
