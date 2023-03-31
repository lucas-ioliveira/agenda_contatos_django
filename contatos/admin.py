from django.contrib import admin
from .models import Categoria, Contato


# Modificando exibição
class ContatoAdmin(admin.ModelAdmin):
    # Exibição
    list_display = (
        "id",
        "nome",
        "sobrenome",
        "telefone",
        "email",
        "data_criacao",
        "categoria",
        "mostrar",
    )
    # Clicaveis para edição
    list_display_links = ("id", "nome")
    # Filtros
    # list_filter = ('id', 'nome')
    # Paginação
    list_per_page = 10
    # Filtros
    search_fields = ("nome", "sobrenome", "telefone")
    # Edição sem entrar no contato
    list_editable = ("telefone", "mostrar")


# Registrando os modelos no admin do Django.
admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
