from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from projects import models


class ViewAllProjects(View):
    def get(self, request):
        projects = models.Project.objects.active()
        return render(request, 'projects/all_projects.html', {'projects': projects})


class ViewProject(View):
    def get(self, request, slug):
        projects = models.Project.objects.active()
        project = get_object_or_404(models.Project, active=True, slug=slug)
        return render(
            request, 'projects/project.html', {'project': project, 'projects': projects}
        )


class ProjectGallery(View):
    def get(self, request, slug, pk):
        projects = models.Project.objects.active()
        project = get_object_or_404(models.Project, active=True, slug=slug)
        total = project.photos.count()
        return render(
            request,
            'projects/gallery.html',
            {
                'project': project,
                'projects': projects,
                'photos': project.photos.active(),
                'total': total,
            },
        )
