from django.contrib import admin
from .models import Adresse, Baccalaureat, Info_personnel, Student_file

# Register your models here.


@admin.register(Info_personnel)
class Info_personnelAdmin(admin.ModelAdmin):
    list_display = ['nom', 'nationalite', 'civilite', 'pays_naissance']
    list_filter = ('pays_naissance',)


@admin.register(Adresse)
class AdresseAdmin(admin.ModelAdmin):
    list_display = ['pays', 'email', ]
    list_filter = ('pays',)


@admin.register(Baccalaureat)
class BaccalaureatAdmin(admin.ModelAdmin):
    list_display = ['serie_bac', 'mention', ]
    list_filter = ('mention', 'serie_bac',)


@admin.register(Student_file)
class Student_fileAdmin(admin.ModelAdmin):
    list_display = ['naissance', 'bac_premiere', 'bac_deuxieme']
