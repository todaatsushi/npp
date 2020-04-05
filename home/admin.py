from django.contrib import admin

from home import models as home_models
from projects.admin import ManageActiveMixin


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


class TopicAdmin(ManageActiveMixin, admin.ModelAdmin):
    fields = [
        'name', 'slug', 'active'
    ]
    actions = [
        'activate', 'deactivate'
    ]


class MessageAdmin(admin.ModelAdmin):
    def mark_seen(self, request, queryset):
        for instance in queryset:
            instance.seen = True
            instance.save
        self.message_user(
            request,
            'Succesfully marked as seen.'
        )

    def mark_unseen(self, request, queryset):
        for instance in queryset:
            instance.seen = False
            instance.save
        self.message_user(
            request,
            'Succesfully marked as unseen.'
        )
    
    fieldsets = (
        (None, {
            'fields': ['topic']
        }),
        ('Management', {
            'fields': ['seen', 'notes']
        })
    )

    readonly_fields = [
        'subject', 'message', 'sent_at'
    ]
    actions = [
        'mark_seen', 'mark_unseen'
    ]


admin.site.register(home_models.ContactSettings, ContactSettingsAdmin)
admin.site.register(home_models.Topic, TopicAdmin)
admin.site.register(home_models.Message, MessageAdmin)
