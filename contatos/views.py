# Importação dos módulos do Django para renderizar meu html e levantamento de erros
from django.shortcuts import render, get_object_or_404, redirect

# Importação levantamento de erros
from django.http import Http404

# Importação do meu módulo de contato
from .models import Contato

# Importação do módulo do Django para paginação
from django.core.paginator import Paginator

# Importação do módulo do Django para melhorar a consulta.
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages


# Função que pega todos os meus contatos no banco de dados, exibição com uma paginação e filtra trazendo só os ativos.
def index(request):
    contatos = Contato.objects.order_by("id").filter(mostrar=True)
    paginator = Paginator(contatos, 3)
    page = request.GET.get("p")
    contatos = paginator.get_page(page)
    return render(request, "contatos/index.html", {"contatos": contatos})


# Função que pega um dado no banco de dados e se não existir levanta um erro 404.
def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404()
    return render(request, "contatos/ver_contato.html", {"contato": contato})


# Função que pega um dado no banco de dados filtrando pelo nome.
def busca(request):
    termo = request.GET.get("termo")
    # Tratando excessões e levantando erros.
    if termo is None or not termo:
        messages.add_message(
            request, messages.ERROR, "Campo termo não pode ficar vazio."
        )
        return redirect("index")
    else:
        messages.add_message(request, messages.SUCCESS, "Sucesso..")

    campos = Concat("nome", Value(" "), "sobrenome")
    contatos = Contato.objects.annotate(nome_completo=campos).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    """
    (__icontains) serve para que não precise digitar todo o nome para ser aplicado o filtro
    """

    paginator = Paginator(contatos, 3)
    page = request.GET.get("p")
    contatos = paginator.get_page(page)
    return render(request, "contatos/busca.html", {"contatos": contatos})
