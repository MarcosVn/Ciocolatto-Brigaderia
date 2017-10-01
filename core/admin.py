# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Evento
# Register your models here.


admin.site.site_header = u"Administração da Ciocolatto"
admin.site.index_title = u"Administração da Ciocolatto"
admin.site.site_title = u"Site de Administração da Ciocolatto"

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')

admin.site.register(Evento, EventoAdmin)


