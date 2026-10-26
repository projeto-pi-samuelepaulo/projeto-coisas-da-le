from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "email",
            "password1",
            "password2",
        )
        labels = {
            "username": "Nome de usuário",
            "first_name": "Seu nome",
        }
        help_texts = {
            "username": "",
            "password1": "",
            "password2": "",
        }


class CompraForm(forms.Form):
    quantidade = forms.IntegerField(
        min_value=1,
        label="Quantidade",
        initial=1
    )
    nome_entrega = forms.CharField(
        max_length=120,
        label="Nome para entrega"
    )
    telefone = forms.CharField(
        max_length=25,
        label="Telefone para contato"
    )
    endereco_entrega = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3}),
        label="Endereço ou instruções para retirada"
    )