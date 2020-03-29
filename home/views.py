from django.shortcuts import render
from django.views.generic import View

from home import models


class Home(View):
    def get(self, request):
        projects = models.Project.objects.filter(active=True)
        return render(request, 'home/home.html', {'projects': projects})


class About(View):
    def get(self, request):
        projects = models.Project.objects.filter(active=True)
        return render(request, 'home/about.html', {'projects': projects})


class Contact(View):
    def get(self, request):
        projects = models.Project.objects.filter(active=True)
        return render(request, 'home/contact.html', {'projects': projects})


# TODO - SPLIT INTO PROJECTS APP
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
