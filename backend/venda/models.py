from django.db import models
from django.utils.translation import gettext as _

from produto.models import Produto


class Venda(models.Model):

    produtos = models.ForeignKey(Produto, on_delete=models.PROTECT)
    data = models.DateTimeField(_("Data da venda"), auto_now_add=True)
    total = models.DecimalField(
        _("Valor total da venda"), max_digits=99, decimal_places=2)

    class Meta:
        verbose_name = _('Venda')
        verbose_name_plural = _('Vendas')

    def __str__(self):
        return self.data
    


class Item(models.Model):
    produto = models.ForeignKey(Produto, verbose_name=_("Produto"), on_delete=models.PROTECT)
    venda = models.ForeignKey(Venda, verbose_name=_("Venda"), on_delete=models.PROTECT)
    nome = models.CharField(max_length=200)
    quantidade = models.PositiveIntegerField(default=1)
    preco = models.DecimalField(
        _("preço do produto"), max_digits=99, decimal_places=2, editable=False)
    imagem = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    