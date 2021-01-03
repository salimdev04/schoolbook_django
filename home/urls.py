from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>',
         views.campus_detail, name='campus_detail'),
    path('<int:id>/<slug:slug>/', views.campus_per_pays, name='campus_per_pays'),
]
