from django.shortcuts import render, get_object_or_404

# Levantando erro 404 (forma 'crua')
from django.http import Http404

# importando o meu model
from .models import Contato

# Paginação
from django.core.paginator import Paginator


# Função que coleta todos os meus dados do db | paginação
def index(request):
    # Para coleta todos os dados do meu bd.
    contatos = Contato.objects.all()
    # Define a paginação e quantidades.
    paginator = Paginator(contatos, 3)
    # Coletando a pagina.
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    # Retorno dos dados
    return render(
        request,
        "contatos/index.html",
        # Passo a chave e o valor (contém todos os dados).
        {"contatos": contatos},
    )


# Levantando erro 404 (forma 'crua')
# def ver_contato(request, contato_id):
#     try:
#         # Para pegar um dado do meu bd.
#         contato = Contato.objects.get(id=contato_id)
#         # Retorno do dado
#         return render(
#             request,
#             "contatos/ver_contato.html",
#             {"contato": contato},  # Passo a chave e o valor (contém todos os dados).
#         )
#     except Contato.DoesNotExist as e:
#         raise Http404


# Levantando erro 404 (forma 'convêncional')
def ver_contato(request, contato_id):
    # Para pegar um dado do meu bd| tratando erros
    contato = get_object_or_404(Contato, id=contato_id)
    # Retorno do dado
    return render(
        request,
        "contatos/ver_contato.html",
        {"contato": contato},  # Passo a chave e o valor (contém todos os dados).
    )
