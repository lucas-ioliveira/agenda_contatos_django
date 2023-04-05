from django.db import models
# Importando módulo de contatos
from contatos.models import Contato
# Importação do forms do django
from django import forms


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('mostrar',)
