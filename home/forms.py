from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from home.models import ContactSettings, AboutSettings


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
        cleaned_data.get('message'),
    )


def generate_and_send_mail(data):
    send_mail(
        'Email from {} - {}'.format(data.get('name'), data.get('subject')),
        create_message_body(data),
        settings.EMAIL_HOST_USER,
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Name', 'class': 'contact-form-left'}
        )
    )
    contact_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email', 'class': 'contact-form-left'}
        )
    )

    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Subject', 'class': 'contact-form-left'}
        )
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Your message here', 'class': 'contact-form-right'}
        )
    )


class ContactSettingsForm(forms.ModelForm):
    class Meta:
        model = ContactSettings
        fields = ['on_holiday', 'contact_message', 'thanks_message', 'holiday_message']
        widgets = {
            'email_address': forms.EmailInput(),
        }

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class AboutSettingsForm(forms.ModelForm):
    class Meta:
        model = AboutSettings
        fields = ['email_address', 'phone_number', 'profile']
        widgets = {'email_address': forms.EmailInput()}
