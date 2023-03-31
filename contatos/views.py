from django.shortcuts import render
# importando o meu model
from .models import Contato


def index(request):
    # Para pegar todos os dados do meu bd.
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html',
                  {   # Passo a chave e o valor (contém todos os dados).
                      'contatos': contatos
                  })
