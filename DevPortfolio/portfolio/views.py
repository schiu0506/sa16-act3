from django.shortcuts import render
from .models import Project, Contact

def home(request):
    projects = Project.objects.all()
    return render(request, 'devproject/home.html', {'projects': projects})

def about(request):
    return render(request, 'devproject/about.html')

def work(request):
    project1 = Project.objects.get(pk=1)
    project2 = Project.objects.get(pk=2)
    project3 = Project.objects.get(pk=3)

    return render(request, 'devproject/work.html', {'project1': project1, 'project2': project2, 'project3': project3})

def contact(request):
    return render(request, 'devproject/contact.html')

