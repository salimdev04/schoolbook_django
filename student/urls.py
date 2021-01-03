from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.info_personnel, name="profile"),
    path("adresse/", views.adresse, name="adresse"),
    path("baccalaureat/", views.baccalaureat, name="baccalaureat"),
    path("files/", views.sttudent_files, name="files"),
]
