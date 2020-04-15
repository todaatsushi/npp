from django.contrib import admin

from home import models as home_models
from home.forms import ContactSettingsForm, AboutSettingsForm


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


class AboutSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Contact Details', {
            'fields': ['email_address', 'phone_number']
        }),
        ('Infomation', {
            'fields': ['page_title', 'profile']
        })
    )
    form = AboutSettingsForm


admin.site.register(home_models.ContactSettings, ContactSettingsAdmin)
admin.site.register(home_models.AboutSettings, AboutSettingsAdmin)
