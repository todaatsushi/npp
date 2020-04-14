from django.contrib import admin

from projects import forms
from projects import models as project_models
from projects import utils


class ProjectAdmin(utils.ManageActiveMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['name', 'year', 'active'],
        }),
        ('Meta', {
            'fields': ['date_added', 'last_updated'],
        })
    )
    list_display = ['name', 'year', 'date_added', 'last_updated', 'active']
    list_filter = ['year', 'active']
    form = forms.ProjectForm



class PhotoAdmin(utils.ManageActiveMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['name', 'image', ],
        }),
        ('Photo Information', {
            'fields': ['title', 'caption', 'date_taken', ],
        }),
        ('Project Infomation', {
            'fields': ['project', 'order', ]
        }),
        ('Meta', {
            'fields': ['date_added', 'last_updated', ],
        })
    )
    list_display = ['title', 'date_taken', 'last_updated', 'order', ]
    list_filter = ['project__year', 'project__name', 'order', ]

    form = forms.PhotoForm


admin.site.register(project_models.Project, ProjectAdmin)
admin.site.register(project_models.Photo, PhotoAdmin)
