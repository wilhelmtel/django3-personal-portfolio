from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def intro(request):
    projects = Project.objects.all()
    return render(request, 'homes.html', {'projects':projects})


# Create your views here.
