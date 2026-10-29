from django.contrib import admin
from .models import Roupa, Pedido, ItemPedido


@admin.register(Roupa)
class RoupaAdmin(admin.ModelAdmin):
    list_display = (
        "nome",
        "categoria",
        "tamanho",
        "preco",
        "estoque",
        "ativa",
    )
    list_filter = ("categoria", "tamanho", "ativa")
    search_fields = ("nome", "descricao", "categoria")
    list_editable = ("preco", "estoque", "ativa")


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ("roupa", "quantidade", "preco_unitario")


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("id", "cliente", "criado_em", "status")
    list_filter = ("status", "criado_em")
    search_fields = ("cliente__username", "nome_entrega", "telefone")
    inlines = [ItemPedidoInline]
    readonly_fields = (
        "cliente",
        "nome_entrega",
        "telefone",
        "endereco_entrega",
        "criado_em",
    )