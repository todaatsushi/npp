from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from projects import models
from home import forms


class Home(View):
    def get(self, request):
        return redirect(reverse('all_projects'))


class About(View):
    def get(self, request):
        projects = models.Project.objects.filter(active=True)
        return render(request, 'home/about.html', {'projects': projects})


class Contact(View):
    def get(self, request):
        form = forms.ContactForm
        projects = models.Project.objects.filter(active=True)
        return render(request, 'home/contact.html', {
            'projects': projects, 'form': form
        })
