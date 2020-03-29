from django.shortcuts import render
from django.views.generic import View

from projects import models


class ViewAllProjects(View):
    def get(self, request):
        projects = models.Project.objects.filter(active=True)
        return render(request, 'home/home.html', {'projects': projects})


class ViewProject(View):
    def get(self, request):
        projects = models.Project.objects.filter(active=True)
        return render(request, 'home/home.html', {'projects': projects})


class ViewPhoto(View):
    def get(self, request):
        projects = models.Project.objects.filter(active=True)
        return render(request, 'home/home.html', {'projects': projects})
