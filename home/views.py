from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from projects import models
from home import forms
from home.models import ContactSettings


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
            'projects': projects, 'form': form, 'settings': ContactSettings.objects.first()
        })

    def post(self, request):
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            forms.generate_and_send_mail(form.cleaned_data)
            messages.success(
                request,
                ContactSettings.objects.get().thanks_message
            )
        return redirect(reverse('contact'))
