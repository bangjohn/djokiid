from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hitung/', views.hitung, name='hitung'),
    ]