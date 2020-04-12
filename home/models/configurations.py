from django.db import models


class ContactSettings(models.Model):
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
        if not self.pk and ContactSettings.objects.exists():
            raise Exception('There can only be one Contact configuration!')
        return super().save(*args, **kwargs)


class AboutSettings(models.Model):
    profile = models.TextField(blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    email_address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return 'About Configuration'

    def save(self, *args, **kwargs):
        # There can only be one config!
        if not self.pk and AboutSettings.objects.exists():
            raise Exception('There can only be one About configuration!')
        return super().save(*args, **kwargs)
