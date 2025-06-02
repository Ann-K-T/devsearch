from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Project
# list of dictionaries representing projects
projectList = [
    {
        "id": "1",
        "title": "SmartFarm AI",
        "description": "An AI-powered platform for monitoring crop health and optimizing irrigation.",
    },
    {
        "id": "2",
        "title": "EduPath",
        "description": "An interactive learning platform for personalized student tutoring and progress tracking.",
    },
    {
        "id": "3",
        "title": "HealthTrack",
        "description": "A health app that tracks daily activity, diet, and sleep, offering personalized wellness plans.",
    },
    {
        "id": "4",
        "title": "CityZen",
        "description": "A civic engagement app connecting citizens with local governments for reporting issues and updates.",
    },
    {
        "id": "5",
        "title": "CodeCollab",
        "description": "A real-time collaborative coding environment with integrated video and chat features.",
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-project.html', {'project': projectObj})
