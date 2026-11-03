from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroForm(UserCreationForm):

    email = forms.EmailField(
        required=True,
        label="E-mail"
    )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields["first_name"].required = True

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-input"

    class Meta:
        model = User

        fields = (
            "username",
            "first_name",
            "email",
            "password1",
            "password2"
        )

        labels = {
            "username": "Nome de usuário",
            "first_name": "Seu nome"
        }

        help_texts = {
            "username": "",
            "password1": "",
            "password2": ""
        }


class CompraForm(forms.Form):

    nome_entrega = forms.CharField(
        max_length=120,
        label="Nome completo",
        widget=forms.TextInput(
            attrs={"class": "form-input"}
        )
    )

    telefone = forms.CharField(
        max_length=25,
        label="Telefone",
        widget=forms.TextInput(
            attrs={"class": "form-input"}
        )
    )

    endereco_entrega = forms.CharField(
        label="Endereço para entrega",
        widget=forms.Textarea(
            attrs={
                "class": "form-input",
                "rows": 3
            }
        )
    )