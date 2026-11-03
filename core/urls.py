from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    ClienteLoginView,
    cadastro,
    home,
    produto,
    colecoes,
    novidades,
    contato,
    adicionar_carrinho,
    carrinho,
    atualizar_carrinho,
    remover_carrinho,
    pagamento,
    pedido_confirmado
)

app_name = "core"

urlpatterns = [

    path("", home, name="home"),

    path("colecoes/", colecoes, name="colecoes"),

    path("novidades/", novidades, name="novidades"),

    path("contato/", contato, name="contato"),

    path("produto/<int:produto_id>/", produto, name="produto"),

    path("carrinho/", carrinho, name="carrinho"),

    path(
        "carrinho/adicionar/<int:produto_id>/",
        adicionar_carrinho,
        name="adicionar_carrinho"
    ),

    path(
        "carrinho/atualizar/<int:produto_id>/",
        atualizar_carrinho,
        name="atualizar_carrinho"
    ),

    path(
        "carrinho/remover/<int:produto_id>/",
        remover_carrinho,
        name="remover_carrinho"
    ),

    path("pagamento/", pagamento, name="pagamento"),

    path(
        "pedido/confirmado/",
        pedido_confirmado,
        name="pedido_confirmado"
    ),

    path("conta/entrar/", ClienteLoginView.as_view(), name="login"),

    path("conta/cadastrar/", cadastro, name="cadastro"),

    path("conta/sair/", LogoutView.as_view(), name="logout"),
]