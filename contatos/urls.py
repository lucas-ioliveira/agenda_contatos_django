from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # Criação de um novo endpoint para a visualização de um único contato
    path("<int:contato_id>", views.ver_contato, name="ver_contato"),
]
