from .forms import AdresseForm, BaccalaureatForm, InfoPersoForm, FilesForm
from django.shortcuts import render
from .models import Adresse, Baccalaureat, Info_personnel, Student_file

# Create your views here.


def info_personnel(request):
    if request.method == 'GET':
        info_perso_form = InfoPersoForm(request.GET)
        if info_perso_form.is_valid():
            cd = info_perso_form.cleaned_data
            Info_personnel.objects.create(
                nom=cd['nom'], prenom=cd['prenom'], nationalite=cd['nationalite'], civilite=cd['civilite'], phone=cd['phone'], date_naissance=cd['date_naissance'], pays_naissance=cd['pays_naissance'], ville_naissance=cd['ville_naissance'], user=request.user)

            print("Nom:", cd['nom'])

    else:
        info_perso_form = InfoPersoForm()
    return render(request, 'student/profile.html', {
        'info_perso_form': info_perso_form
    })


def adresse(request):
    if request.method == 'GET':
        adresse_form = AdresseForm(request.GET)
        if adresse_form.is_valid():
            cd = adresse_form.cleaned_data
            Adresse.objects.create(pays=cd['pays'], ville=cd['ville'],
                                   adresse=cd['adresse'], email=cd['email'], user=request.user)
    else:
        adresse_form = AdresseForm()
    return render(request, 'student/adresse.html', {
        'adresse_form': adresse_form
    })


def baccalaureat(request):
    if request.method == 'GET':
        bac_form = BaccalaureatForm(request.GET)
        if bac_form.is_valid():
            cd = bac_form.cleaned_data
            Baccalaureat.objects.create(
                user=request.user, annee=cd['annee'], serie_bac=cd['serie_bac'], mention=cd['mention'], pays_obtention=cd['pays_obtention'])

    else:
        bac_form = BaccalaureatForm()
    return render(request, 'student/baccalaureat.html', {
        'bac_form': bac_form
    })


def sttudent_files(request):
    if request.method == 'GET':
        files_form = FilesForm(request.GET)
        if files_form.is_valid():
            cd = files_form.cleaned_data
            Student_file.objects.create(
                user=request.user, naissance=cd['naissance'], bac_premiere=cd['bac_premiere'], bac_deuxieme=cd['bac_deuxieme'])

    else:
        files_form = FilesForm()
    return render(request, 'student/files.html', {
        'files_form': files_form
    })
