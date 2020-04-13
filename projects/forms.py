from django import forms

from projects import models


class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = [
            'name', 'description', 'year'
        ]

    def save(self, *args, **kwargs):
        slug = self.cleaned_data['name'].replace(' ', '-').lower()
        slug = ''.join(
            [character for character in slug if any([character.isalnum(), character == '-'])]
        )
        self.cleaned_data['slug'] = slug
        unique_slug_flag = bool(
            models.Project.objects.filter(slug=slug)
        )
        if unique_slug_flag:
            raise ValidationError('Project slug must be unique - have you reused the project name?')
        instance = self.instance
        instance.slug = slug
        instance.save()
        return super().save(*args, **kwargs)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = [
            'name', 'image', 'title', 'caption', 'date_taken', 'order', 'project', 'active'
        ]

    def save(self, *args, **kwargs):
        if not self.cleaned_data['image']:
            raise ValidationError('Image cannot be empty')

        # Validate order
        project = models.Project.objects.get(id=self.cleaned_data['project'].id)
        other_photos = project.photos
        if other_photos.filter(order=self.cleaned_data['order']):
            raise forms.ValidationError('Photo in that order position already exists.')

        return super().save(*args, **kwargs)
