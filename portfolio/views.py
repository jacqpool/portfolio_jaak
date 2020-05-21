from django.shortcuts import render
from .models import Project

def home(request):
    return render(request, 'portfolio/home.html')

def all_projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})


    #bogs = Bog.objects.order_by('-date')  #[:4]
