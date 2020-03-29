from django.shortcuts import render
from django.views.generic import (ListView, DetailView, FormView)

from home import models


def home(request):
    projects = models.Project.objects.filter(active=True)
    return render(request, 'home/home.html', {'projects': projects})


def about(request):
    pass


class Contact(FormView):
    pass


class ViewProjects(ListView):
    pass


class ViewProject(DetailView):
    pass


class ViewPhoto(DetailView):
    pass
