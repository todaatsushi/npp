from django import forms
from django.conf import settings
from django.core.mail import send_mail

from home.models import ContactSettings

TOPICS = (
    ('Business', 'Business Enquiry'),
    ('Comment', 'Comment'),
    ('Other', 'Other')
)


class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPICS)

    subject = forms.CharField()
    name = forms.CharField()
    contact_email = forms.EmailField()

    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def save(self, *args, **kwargs):
        send_mail(

        )
        super().save(*args, **kwargs)


class ContactSettingsForm(forms.ModelForm):
    class Meta:
        model = ContactSettings
        fields = [
            'on_holiday', 'contact_message', 'thanks_message', 'holiday_message'
        ]
        widgets = {
            'email_address': forms.EmailInput(),
            'email_password': forms.PasswordInput(),
        }

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
