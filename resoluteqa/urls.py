from django.urls import path

from . import views

app_name = 'resoluteqa'
urlpatterns = [
    path('', views.index, name='index'),
    path('results/summary', views.summary, name='summary'),
    path('results/dailyresults', views.daily, name='daily'),
]
