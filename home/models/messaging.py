from django.db import models
from django.utils import timezone


class Topic(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='The front facing name of the topic.',
    )
    slug = models.CharField(
        max_length=200,
        help_text='This is how the topic is stored in the db.',
    )
    active = models.BooleanField(
        default=True, help_text='Toggle visibility to the users.'
    )


class Message(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subject = models.CharField(
        max_length=200
    )
    message = models.TextField()

    seen = models.BooleanField(default=False)
    sent_at = models.DateTimeField(default=timezone.now)

    notes = models.TextField(
        help_text='Note down any actions you want to take or notes.'
    )
