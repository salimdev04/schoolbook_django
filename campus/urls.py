from django.urls import path
from . import views


app_name = 'campus'

urlpatterns = [
    path('', views.campus_list, name='campus_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>',
         views.campus_detail, name='campus_detail'),
]
