from django.contrib import admin

from home import models as home_models
from home.forms import ContactSettingsForm


class ContactSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Notification settings', {
            'fields': ['on_holiday'],
        }),
        ('Messaging', {
            'fields': ['contact_message', 'thanks_message', 'holiday_message']
        })
    )
    form = ContactSettingsForm


admin.site.register(home_models.ContactSettings, ContactSettingsAdmin)
