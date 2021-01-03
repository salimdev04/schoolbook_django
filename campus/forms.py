from django import forms

from .models import Campus


class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ('pays', 'title', 'type', 'study_level', 'speciality', 'langue', 'site_web',
                  'email', 'region', 'description', 'debut_inscription', 'fin_inscription', 'image')
