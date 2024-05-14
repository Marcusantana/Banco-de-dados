from django.contrib import admin
from django.urls import path, include
from .views import fproduto, salvar, delete, exibir, update

urlpatterns = [
    path('', fproduto),
    path('salvar/', salvar , name='salvar'),
    path('delete/<int:id>', delete, name='delete'),
    path('exibir/<int:id>', exibir, name='exibir'),
    path('update/<int:id>', update, name='update')
]