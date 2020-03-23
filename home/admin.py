from django.contrib import admin

from home import models


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['name', 'year'],
        }),
        ('Meta', {
            'fields': ['date_added', 'last_updated'],
        })
    )
    list_display = ['name', 'year', 'date_added', 'last_updated']
    list_filter = ['year']


class PhotoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['name', 'upload_url', 'project__name',],
        }),
        ('Photo Information', {
            'fields': ['title', 'caption', 'date_taken',],
        }),
        ('Meta', {
            'fields': ['date_added', 'last_updated',],
        })
    )
    list_display = ['title', 'date_taken', 'last_updated']
    list_filter = ['project__year']


admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Photo, PhotoAdmin)
