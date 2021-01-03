from django.forms import fields
from student.models import Adresse, Baccalaureat, Info_personnel, Student_file
from django import forms


class InfoPersoForm(forms.ModelForm):
    class Meta:
        model = Info_personnel
        fields = ('nom', 'prenom', 'nationalite', 'civilite', 'phone',
                  'date_naissance', 'pays_naissance', 'ville_naissance')


class AdresseForm(forms.ModelForm):
    class Meta:
        model = Adresse
        fields = ('pays', 'ville', 'adresse', 'email')


class BaccalaureatForm(forms.ModelForm):
    class Meta:
        model = Baccalaureat
        fields = ('annee', 'serie_bac', 'mention', 'pays_obtention')


class FilesForm(forms.ModelForm):
    class Meta:
        model = Student_file
        fields = ('naissance', 'bac_premiere', 'bac_deuxieme',
                  'licence', 'master', 'doctorat', 'autre1', 'autre2')
