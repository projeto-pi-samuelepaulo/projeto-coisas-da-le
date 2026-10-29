from decimal import Decimal
from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Roupa(models.Model):
    nome = models.CharField(max_length=120)
    descricao = models.TextField(blank=True)
    tamanho = models.CharField(max_length=20)
    categoria = models.CharField(max_length=60)
    preco = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))]
    )
    estoque = models.PositiveIntegerField(default=0)
    imagem = models.ImageField(
        upload_to="produtos/",
        blank=True,
        null=True
    )
    ativa = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return self.nome

    @property
    def disponivel(self):
        return self.ativa and self.estoque > 0


class Pedido(models.Model):
    STATUS_CHOICES = [
        ("aguardando", "Aguardando confirmação"),
        ("confirmado", "Confirmado"),
        ("cancelado", "Cancelado"),
    ]

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="pedidos"
    )
    nome_entrega = models.CharField(max_length=120)
    telefone = models.CharField(max_length=25)
    endereco_entrega = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="aguardando"
    )

    class Meta:
        ordering = ["-criado_em"]

    def __str__(self):
        return f"Pedido #{self.pk} - {self.cliente}"

    @property
    def total(self):
        return sum(
            (item.subtotal for item in self.itens.all()),
            Decimal("0.00")
        )


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        on_delete=models.CASCADE,
        related_name="itens"
    )
    roupa = models.ForeignKey(
        Roupa,
        on_delete=models.PROTECT,
        related_name="itens_pedido"
    )
    quantidade = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    preco_unitario = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))]
    )

    def __str__(self):
        return f"{self.quantidade} x {self.roupa.nome}"

    @property
    def subtotal(self):
        return self.preco_unitario * self.quantidade