from django.shortcuts import render, get_object_or_404, redirect

# Levantando erro 404 (forma 'crua')
from django.http import Http404

# importando o meu model
from .models import Contato

# Paginação
from django.core.paginator import Paginator

# Campo de consulta
from django.db.models import Q, Value
from django.db.models.functions import Concat

# Para menssagens
from django.contrib import messages


# Função que coleta todos os meus dados do db | paginação
def index(request):
    # Para coleta todos os dados do meu bd| Definindo a paginação.
    contatos = Contato.objects.order_by("id").filter(mostrar=True)
    # Define a paginação e quantidades.
    paginator = Paginator(contatos, 3)
    # Coletando a pagina.
    page = request.GET.get("p")
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
    # Tratando erro http404
    if not contato.mostrar:
        raise Http404()
    # Retorno do dado
    return render(
        request,
        "contatos/ver_contato.html",
        {"contato": contato},  # Passo a chave e o valor (contém todos os dados).
    )


# Função de busca
def busca(request):
    # Para coletar o termo do imput
    termo = request.GET.get("termo")

    if termo is None or not termo:
        messages.add_message(
            request, messages.ERROR, "Campo termo não pode ficar vazio."
        )
        return redirect('index')
    else:
        messages.add_message(
            request, messages.SUCCESS, 'Sucesso!'
        )

    # Para concatenar o termo
    campos = Concat("nome", Value(" "), "sobrenome")

    # Para coleta o termo na views e buscar o dado no db.
    contatos = Contato.objects.annotate(nome_completo=campos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo),
    )

    # Define a paginação e quantidades.
    paginator = Paginator(contatos, 3)

    # Coletando a pagina.
    page = request.GET.get("p")
    contatos = paginator.get_page(page)

    # Retorno dos dados
    return render(
        request,
        "contatos/busca.html",
        # Passo a chave e o valor (contém todos os dados).
        {"contatos": contatos},
    )
