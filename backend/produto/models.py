from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Produto(models.Model):
    comprador = models.ForeignKey(User, on_delete=models.PROTECT)
    nome = models.CharField(_('Nome do produto'), max_length=50)
    preco = models.DecimalField(
        _('Preço do produto'), decimal_places=2, max_digits=99)
    preco_oferta = models.DecimalField(
        _('Preço do produto em oferta'), decimal_places=2, max_digits=99, default=0.00)
    marca = models.CharField(_("Marca"), max_length=50)
    categoria = models.CharField(_("Categoria"), max_length=50)

    previsão_entrega = models.PositiveSmallIntegerField(
        _('Previsão da entrega em dias'))
    data_prevista_entrega = models.DateField(
        _("Data prevista para entrega"), auto_now=False, auto_now_add=False)
    sku = models.CharField(max_length=50)
    quantidade_estoque = models.IntegerField(
        _("Quantidade em estoque"), default=0)
    # imagem

    class Meta:
        verbose_name = _("produto")
        verbose_name_plural = _("produtos")

    def __str__(self):
        return self.nome
