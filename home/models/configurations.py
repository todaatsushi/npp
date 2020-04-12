from django.db import models


class ContactSettings(models.Model):
    email_address = models.EmailField(
        max_length=100,
        blank=True,
        null=True,
        help_text='This should be the email you would like to recieve notifcations to.'
        )
    email_password = models.CharField(max_length=100, blank=True, null=True)

    on_holiday = models.BooleanField(
        default=False,
        help_text='Set this to True if you will not be replying for a while.'
    )

    contact_message = models.TextField(
        help_text='This is the message that shows on the contact page before they get in touch.'
    )
    thanks_message = models.TextField(
        help_text='This is the message that shows when they succesfully send you a message.'
    )
    holiday_message = models.TextField(
        help_text='This is the message that shows to notify you will not be replying for a while.'
    )

    def __str__(self):
        return 'Contact Configuration'

    def save(self, *args, **kwargs):
        # There can only be one config!
        if any([
            self.pk,
            ContactSettings.objects.count(),
        ]):
            raise Exception('There can only be one Contact configuration!')
        return super().save(*args, **kwargs)
