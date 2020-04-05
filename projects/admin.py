from django.contrib import admin

from projects import models


class ManageActiveMixin:

    actions = ['activate', 'deactivate']

    def activate(self, request, queryset):
        for instance in queryset:
            instance.active = True
            instance.save()
        self.message_user(
            request, 'Successfully activated instances.'
        )

    def deactivate(self, request, queryset):
        for instance in queryset:
            instance.active = False
            instance.save()
        self.message_user(
            request, 'Successfully deactivated instances.'
        )

    activate.short_description = (
        'Turn on \'active\' of all selected.'
    )

    deactivate.short_description = (
        'Turn off \'active\' of all selected.'
    )


class ProjectAdmin(ManageActiveMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['name', 'year', 'active', 'slug'],
        }),
        ('Meta', {
            'fields': ['date_added', 'last_updated'],
        })
    )
    list_display = ['name', 'year', 'date_added', 'last_updated', 'active']
    list_filter = ['year']



class PhotoAdmin(ManageActiveMixin, admin.ModelAdmin):
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
