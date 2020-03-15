from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    def save(self):
        self.last_updated = timezone.now()
        super().save()


class Photo(models.Model):
    name = models.CharField(max_length=50)
    upload_url = models.CharField(max_length=200)

    # Photo information
    title = models.CharField(blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    date_taken = models.DateTimeField(blank=True, null=True)

    date_added = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    def save(self):
        self.last_updated = timezone.now()
        super().save()
