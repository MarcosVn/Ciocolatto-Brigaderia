# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from decimal import Decimal
from django.conf import settings

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300, verbose_name='Link completo do Facebook:')
    data = models.DateField()
    foto = models.ImageField()

    class Meta:
        ordering = ['-data']
        verbose_name = u'Evento'
        verbose_name_plural = u'Eventos'


class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=800)
    preco = models.DecimalField(max_digits=20, decimal_places=2, default=Decimal('0.00'))
    data_add = models.DateTimeField(u'Data de cadastro', auto_now_add=True, null=True, blank=True)

    def get_primeira_foto(self):
        if self.fotoproduto_set.count():
            return self.fotoproduto_set.all().order_by('id')[0]
        else:
            return None

    def get_fotos(self):
        return self.fotoproduto_set.all().order_by('id')


class FotoProduto(models.Model):
    produto = models.ForeignKey(Produto)
    foto = models.ImageField()
    data_add = models.DateTimeField(u'Data de cadastro', auto_now_add=True, null=True, blank=True)


class Parceiro(models.Model):
    nome = models.CharField(max_length=200, verbose_name='Nome do Paceiro ')
    endereco = models.CharField(max_length=400, verbose_name='Endereço')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    facebook = models.CharField(max_length=800, verbose_name='Link para Facebook')
    foto = models.ImageField()
    data_add = models.DateTimeField(u'Data de cadastro', auto_now_add=True, null=True, blank=True)




