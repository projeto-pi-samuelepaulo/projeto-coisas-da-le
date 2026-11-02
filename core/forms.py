from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CadastroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="E-mail")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["username"].widget.attrs.update(
            {"autocomplete": "username"}
        )
        self.fields["first_name"].widget.attrs.update(
            {"autocomplete": "given-name"}
        )
        self.fields["email"].widget.attrs.update(
            {"autocomplete": "email", "type": "email"}
        )
        self.fields["password1"].widget.attrs.update(
            {"autocomplete": "new-password"}
        )
        self.fields["password2"].widget.attrs.update(
            {"autocomplete": "new-password"}
        )
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-input"

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