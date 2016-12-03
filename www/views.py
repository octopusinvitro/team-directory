from django.shortcuts import render
from .models import Person


def index(request):
    context = {'persons': Person.objects.all()}
    return render(request, 'index.html', context)
