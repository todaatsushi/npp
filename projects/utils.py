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
