from django.db import models
from django.utils import timezone


class ActiveObjectsMixin:
    def active(self):
        return self.filter(active=True)


class ProjectManager(ActiveObjectsMixin, models.Manager):
    pass


class PhotoManager(ActiveObjectsMixin, models.Manager):
    pass



class Project(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=30)

    description = models.TextField(blank=True, null=True)

    year = models.IntegerField(null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    active = models.BooleanField(default=False)

    objects = ProjectManager()

    def save(self):
        self.last_updated = timezone.now()
        super().save()

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return f'{self.name} - {self.year}'


class Photo(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True
    )

    # Photo information
    title = models.CharField(blank=True, null=True, max_length=100)
    caption = models.TextField(blank=True, null=True)
    date_taken = models.DateTimeField(blank=True, null=True)
    order = models.IntegerField()

    date_added = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    project = models.ForeignKey(
        'Project', on_delete=models.CASCADE, related_name='photos'
    )
    active = models.BooleanField(default=False)

    objects = PhotoManager()

    def save(self):
        self.last_updated = timezone.now()
        return super().save()

    def __repr__(self):
        return self.name
    
    def __str__(self):
        return f'{self.name} - {self.last_updated}'
