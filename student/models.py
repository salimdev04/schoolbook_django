from django.db import models
from django.conf import settings

# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.username, filename)


class Info_personnel(models.Model):
    CIVILITE_CHOICE = (
        ('Masculin', 'Masculin'),
        ('Feminin', 'Feminin'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    nationalite = models.CharField(max_length=250)
    civilite = models.CharField(
        max_length=9, choices=CIVILITE_CHOICE, default='Masculin')
    phone = models.CharField(max_length=250)
    date_naissance = models.DateField()
    pays_naissance = models.CharField(max_length=250)
    ville_naissance = models.CharField(max_length=250)

    def __str__(self):
        return self.nom


class Adresse(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    pays = models.CharField(max_length=250)
    ville = models.CharField(max_length=250)
    adresse = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.pays


class Baccalaureat(models.Model):
    MENTION_BAC = (
        ('Tres Bien', 'Tres Bien'),
        ('Bien', 'Bien'),
        ('Assez Bien', 'Assez Bien'),
        ('Passable', 'Passable'),
    )

    SERIE_BAC = (
        ('S-Scientifique', 'S-Scientifique'),
        ('S-Litteraire', 'S-Litteraire'),
        ('S-Technique', 'S-Technique'),
    )

    ANNEE_BAC = (
        (i, i) for i in range(2000, 2023)
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    annee = models.IntegerField(choices=ANNEE_BAC)
    serie_bac = models.CharField(max_length=15, choices=SERIE_BAC)
    mention = models.CharField(max_length=12, choices=MENTION_BAC)
    pays_obtention = models.CharField(max_length=50)

    def __str__(self):
        return self.serie_bac


class Student_file(models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    naissance = models.FileField(upload_to=user_directory_path)
    bac_premiere = models.FileField(upload_to=user_directory_path)
    bac_deuxieme = models.FileField(upload_to=user_directory_path)
    licence = models.FileField(
        upload_to=user_directory_path, null=True, blank=True)
    master = models.FileField(
        upload_to=user_directory_path, null=True, blank=True)
    doctorat = models.FileField(
        upload_to=user_directory_path, null=True, blank=True)
    autre1 = models.FileField(
        upload_to=user_directory_path, null=True, blank=True)
    autre2 = models.FileField(
        upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return self.user.username
