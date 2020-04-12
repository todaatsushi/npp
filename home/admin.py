from django.contrib import admin

from home import models as home_models


class ContactSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Email settings', {
            'fields': ['email_address', 'email_password'],
        }),
        ('Notification settings', {
            'fields': ['recieve_notifications', 'on_holiday'],
        }),
        ('Messaging', {
            'fields': ['contact_message', 'thanks_message', 'holiday_message']
        })
    )


admin.site.register(home_models.ContactSettings, ContactSettingsAdmin)
