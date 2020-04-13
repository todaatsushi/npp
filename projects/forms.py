from django import forms

from home import models


class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = [
            'name', 'description', 'year'
        ]

    def save(self, *args, **kwargs):
        slug = self.cleaned_data['name'].replace(' ', '-').lower()
        slug = ''.join(
            [character if any([character.isalnum(), character == '-']) for character in slug]
        )
        self.cleaned_data['slug'] = slug
        return super().save(*args, **kwargs)


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = [
            'name', 'image', 'title', 'caption', 'date_taken', 'order', 'project', 'active'
        ]

    def save(self, *args, **kwargs):
        if not self.cleaned_data['image']:
            raise forms.ValidationError('Image cannot be empty')
        return super().save(*args, **kwargs)
