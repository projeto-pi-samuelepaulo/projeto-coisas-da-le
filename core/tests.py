from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .forms import CadastroForm


class CadastroFormTests(TestCase):
    def test_campos_obrigatorios_sao_validados(self):
        form = CadastroForm(
            data={
                "username": "",
                "first_name": "",
                "email": "",
                "password1": "",
                "password2": "",
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)
        self.assertIn("first_name", form.errors)
        self.assertIn("email", form.errors)
        self.assertIn("password1", form.errors)
        self.assertIn("password2", form.errors)


class ContaClienteTests(TestCase):
    def test_paginas_de_login_e_cadastro_exibem_formularios(self):
        login_response = self.client.get(reverse("core:login"))
        cadastro_response = self.client.get(reverse("core:cadastro"))

        self.assertEqual(login_response.status_code, 200)
        self.assertContains(login_response, "Boas-vindas de volta")
        self.assertContains(login_response, 'name="username"')
        self.assertEqual(cadastro_response.status_code, 200)
        self.assertContains(cadastro_response, "Crie sua conta")
        self.assertContains(cadastro_response, 'name="email"')

    def test_cadastro_cria_cliente_autenticado(self):
        response = self.client.post(
            reverse("core:cadastro"),
            {
                "username": "cliente",
                "first_name": "Cliente",
                "email": "cliente@example.com",
                "password1": "UmaSenhaForte-2026",
                "password2": "UmaSenhaForte-2026",
            },
        )

        self.assertRedirects(response, reverse("core:home"))
        usuario = get_user_model().objects.get(username="cliente")
        self.assertTrue(usuario.check_password("UmaSenhaForte-2026"))
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_superuser)
        self.assertIn("_auth_user_id", self.client.session)

    def test_cadastro_invalido_exibe_erros(self):
        response = self.client.post(
            reverse("core:cadastro"),
            {
                "username": "",
                "first_name": "",
                "email": "",
                "password1": "",
                "password2": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Este campo é obrigatório.")
        self.assertEqual(get_user_model().objects.count(), 0)

    def test_login_com_credenciais_validas(self):
        get_user_model().objects.create_user(
            username="cliente",
            password="UmaSenhaForte-2026",
        )

        response = self.client.post(
            reverse("core:login"),
            {
                "username": "cliente",
                "password": "UmaSenhaForte-2026",
            },
        )

        self.assertRedirects(response, reverse("core:home"))
        self.assertIn("_auth_user_id", self.client.session)

    def test_logout_encerra_sessao(self):
        usuario = get_user_model().objects.create_user(
            username="cliente",
            password="UmaSenhaForte-2026",
        )
        self.client.force_login(usuario)

        response = self.client.post(reverse("core:logout"))

        self.assertRedirects(response, reverse("core:home"))
        self.assertNotIn("_auth_user_id", self.client.session)
