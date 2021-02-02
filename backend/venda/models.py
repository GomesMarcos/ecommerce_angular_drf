from django.db import models
from django.utils.translation import gettext as _

from produto.models import Produto


class Venda(models.Model):

    produtos = models.ForeignKey(Produto, on_delete=models.PROTECT)
    data = models.DateTimeField(_("Data da venda"), auto_now_add=True)
    total = models.DecimalField(
        _("Valor total da venda"), max_digits=99, decimal_places=2)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = 'Vendas'


class Item(models.Model):
    nome = models.CharField(_("nome do produto"), max_length=50)
    preco = models.DecimalField(
        _("preço do produto"), max_digits=99, decimal_places=2, editable=False)
    descricao = models.TextField(_("descrição"))
