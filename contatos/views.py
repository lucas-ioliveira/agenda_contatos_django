from django.shortcuts import render

# importando o meu model
from .models import Contato


# Função que coleta todos os meus dados do db
def index(request):
    # Para coleta todos os dados do meu bd.
    contatos = Contato.objects.all()
    # Retorno dos dados
    return render(
        request,
        "contatos/index.html",
        {"contatos": contatos},  # Passo a chave e o valor (contém todos os dados).
    )


def ver_contato(request, contato_id):
    # Para pegar um dado do meu bd.
    contato = Contato.objects.get(id=contato_id)
    # Retorno do dado
    return render(
        request,
        "contatos/ver_contato.html",
        {"contato": contato},  # Passo a chave e o valor (contém todos os dados).
    )
