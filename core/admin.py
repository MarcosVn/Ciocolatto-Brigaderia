# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Evento, Parceiro, FotoProduto, Produto

admin.site.site_header = u"Administração da Ciocolatto"
admin.site.index_title = u"Administração da Ciocolatto"
admin.site.site_title = u"Site de Administração da Ciocolatto"

class FotoProdutoInline(admin.TabularInline):
    model = FotoProduto

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')

class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco')

    inlines = [
        FotoProdutoInline
    ]

admin.site.register(Evento, EventoAdmin)
admin.site.register(Parceiro, ParceiroAdmin)
admin.site.register(Produto, ProdutoAdmin)


