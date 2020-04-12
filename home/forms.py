from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from home.models import ContactSettings

TOPICS = (
    ('Business', 'Business Enquiry'),
    ('Comment', 'Comment'),
    ('Other', 'Other')
)

def create_message_body(cleaned_data):
    return '''
        Sent at: {}
        From: {} - {}

        Subject: {}

        {}
    '''.format(
        timezone.now(),
        cleaned_data.get('name'),
        cleaned_data.get('contact_email'),
        cleaned_data.get('subject'),
        cleaned_data.get('message')
    )


def generate_and_send_mail(data):
    send_mail(
        'Email from {} - {}'.format(
            data.get('name'), data.get('subject')
        ),
        create_message_body(data),
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False
    )


class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPICS)

    name = forms.CharField()
    contact_email = forms.EmailField()

    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


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
