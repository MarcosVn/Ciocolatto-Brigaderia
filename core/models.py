# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.conf import settings


# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300, verbose_name='Link completo do Facebook:')
    data = models.DateField()
    foto = models.ImageField(upload_to='ciocolatto/static/img')

    class Meta:
        ordering = ['-data']
        verbose_name = u'Evento'
        verbose_name_plural = u'Eventos'