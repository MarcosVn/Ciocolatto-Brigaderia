# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Evento
# Register your models here.


class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')

admin.site.register(Evento, EventoAdmin)


