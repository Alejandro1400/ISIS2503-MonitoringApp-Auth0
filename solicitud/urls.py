from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cargar/', views.upload, name='cargar'),
    path('archivos/', views.archivos_view, name='archivos'),
    path('archivo/<int:pk>', views.archivo_view, name='archivo'),
]