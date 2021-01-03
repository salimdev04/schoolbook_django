from django import forms
from .models import Admission


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = ('campus',)
