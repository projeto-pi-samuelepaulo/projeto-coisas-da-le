from decimal import Decimal

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render

from .forms import CadastroForm, CompraForm
from .catalogo import PRODUTOS


class ClienteLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = AuthenticationForm


def cadastro(request):
    if request.user.is_authenticated:
        return redirect("core:home")

    form = CadastroForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        usuario = form.save()
        login(request, usuario)

        messages.success(
            request,
            f"Bem-vinda, {usuario.first_name}! Seu cadastro foi concluído."
        )

        return redirect("core:home")

    return render(
        request,
        "registration/signup.html",
        {"form": form}
    )


def home(request):
    return render(
        request,
        "index.html",
        {"produtos": PRODUTOS[:3]}
    )


def colecoes(request):
    categoria = request.GET.get("categoria", "")

    produtos = PRODUTOS

    if categoria:
        produtos = [
            p for p in PRODUTOS
            if p["categoria"] == categoria
        ]

    categorias = sorted(
        set(p["categoria"] for p in PRODUTOS)
    )

    return render(request, "colecoes.html", {
        "produtos": produtos,
        "categorias": categorias,
        "categoria_atual": categoria
    })


def novidades(request):
    return render(
        request,
        "novidades.html",
        {"produtos": PRODUTOS[-6:]}
    )


def contato(request):
    return render(request, "contato.html")


def produto(request, produto_id):
    item = next(
        (p for p in PRODUTOS if p["id"] == produto_id),
        None
    )

    if item is None:
        return redirect("core:colecoes")

    return render(
        request,
        "product.html",
        {"produto": item}
    )



def adicionar_carrinho(request, produto_id):

    if request.method == "POST":

        item = next(
            (p for p in PRODUTOS if p["id"] == produto_id),
            None
        )

        if item:
            carrinho = request.session.get("carrinho", {})

            chave = str(produto_id)

            carrinho[chave] = carrinho.get(chave, 0) + 1

            request.session["carrinho"] = carrinho

            messages.success(
                request,
                f"{item['nome']} foi adicionado ao carrinho."
            )

    return redirect(
        request.META.get("HTTP_REFERER", "core:colecoes")
    )



def carrinho(request):

    dados = []

    carrinho_atual = request.session.get("carrinho", {})

    total = Decimal("0.00")

    for produto_id, quantidade in carrinho_atual.items():

        item = next(
            (p for p in PRODUTOS if p["id"] == int(produto_id)),
            None
        )

        if item:
            subtotal = Decimal(item["preco"]) * quantidade

            dados.append({
                "produto": item,
                "quantidade": quantidade,
                "subtotal": subtotal
            })

            total += subtotal

    return render(request, "carrinho.html", {
        "itens": dados,
        "total": total
    })



def atualizar_carrinho(request, produto_id):

    if request.method == "POST":

        carrinho_atual = request.session.get("carrinho", {})

        quantidade = int(request.POST.get("quantidade", 1))

        if quantidade <= 0:
            carrinho_atual.pop(str(produto_id), None)
        else:
            carrinho_atual[str(produto_id)] = min(quantidade, 20)

        request.session["carrinho"] = carrinho_atual

    return redirect("core:carrinho")



def remover_carrinho(request, produto_id):

    if request.method == "POST":

        carrinho_atual = request.session.get("carrinho", {})

        carrinho_atual.pop(str(produto_id), None)

        request.session["carrinho"] = carrinho_atual

    return redirect("core:carrinho")



def pagamento(request):

    carrinho_atual = request.session.get("carrinho", {})

    if not carrinho_atual:
        messages.info(
            request,
            "Adicione pelo menos um produto antes de finalizar a compra."
        )
        return redirect("core:colecoes")

    total = sum(
        (
            Decimal(
                next(
                    p for p in PRODUTOS
                    if p["id"] == int(pid)
                )["preco"]
            ) * qtd
            for pid, qtd in carrinho_atual.items()
        ),
        Decimal("0.00")
    )

    form = CompraForm(request.POST or None)

    if request.method == "POST" and form.is_valid():

        pedido = {
            "nome": form.cleaned_data["nome_entrega"],
            "telefone": form.cleaned_data["telefone"],
            "endereco": form.cleaned_data["endereco_entrega"],
            "pagamento": request.POST.get("forma_pagamento", "Pix"),
            "total": str(total)
        }

        request.session["ultimo_pedido"] = pedido

        request.session["carrinho"] = {}

        return redirect("core:pedido_confirmado")

    return render(request, "pagamento.html", {
        "form": form,
        "total": total
    })



def pedido_confirmado(request):

    pedido = request.session.get("ultimo_pedido")

    if not pedido:
        return redirect("core:home")

    return render(
        request,
        "pedido_confirmado.html",
        {"pedido": pedido}
    )