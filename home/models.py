from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=30)

    year = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    active = models.BooleanField(default=False)

    def save(self):
        self.last_updated = timezone.now()
        super().save()

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return f'{self.name} - {self.year}'


class Photo(models.Model):
    name = models.CharField(max_length=50)
    upload_url = models.CharField(max_length=200)

    # Photo information
    title = models.CharField(blank=True, null=True, max_length=100)
    caption = models.TextField(blank=True, null=True)
    date_taken = models.DateTimeField(blank=True, null=True)
    order = models.IntegerField()

    date_added = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def save(self):
        self.last_updated = timezone.now()
        super().save()

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return f'{self.name} - {self.last_updated}'
