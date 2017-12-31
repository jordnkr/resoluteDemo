from django.urls import path

from . import views

app_name = 'resoluteqa'
urlpatterns = [
    path('', views.index, name='index'),
]
