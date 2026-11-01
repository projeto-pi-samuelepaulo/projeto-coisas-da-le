from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    ClienteLoginView,
    cadastro,
    home,
    produto,
)

app_name = "core"

urlpatterns = [
    path("", home, name="home"),
    path("produto/<int:produto_id>/", produto, name="produto"),
    path("conta/entrar/", ClienteLoginView.as_view(), name="login"),
    path("conta/cadastrar/", cadastro, name="cadastro"),
    path("conta/sair/", LogoutView.as_view(), name="logout"),
]
