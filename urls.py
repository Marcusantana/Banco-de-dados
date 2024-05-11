from django.contrib import admin
from django.urls import path, include
from .views import fcliente, salvar, delete

urlpatterns = [
    path('', fcliente),
    path('salvar/', salvar , name='salvar'),
    path('delete/<int:id>', delete, name='delete'),
]