from __future__ import unicode_literals
from django.db import models
from django.utils.safestring import mark_safe

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = u'Fornecedor'
        verbose_name_plural = u'FORNECEDOR'
        


class Material(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = u'Material'
        verbose_name_plural = u'MATERIAL'

class Compra(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    nota_fiscal = models.CharField(max_length=10)
    data = models.DateField()
    valor_compra = models.DecimalField(max_digits=10,
    decimal_places=2, blank=True, default=0)

    def imprimir(self):
            return mark_safe("""<a href=\"/orcamento/%s/\" target="_blank"><img src=\"/static/images/b_print.png\"></a>""" % self.id)

    class Meta:
        verbose_name = u'Compra'
        verbose_name_plural = u'COMPRAS'
        ordering = ['-data']

class Produto(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    preco = models.DecimalField(u'PREÇO',max_digits=15,decimal_places=2)
    quantidade = models.DecimalField(u'QUANTIDADE', max_digits=5,decimal_places=0)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2,
    editable=False)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)

    def __str__(self):
        return self.material.nome + ",R$" + str(self.preco) +"," + str(self.quantidade) + ",R$" + str(self.subtotal)

    class Meta:
        verbose_name = u'Produto'
        verbose_name_plural = u'PRODUTOS'

    #calculo
    def save(self, *args, **kwargs):
    	self.subtotal = self.preco * self.quantidade 
    	self.compra.valor_compra += self.subtotal
    	self.compra.save()
    	return super(Produto, self).save(*args, **kwargs)
