# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def home(request):
        context = {'texto': 'Contexto teste'}
        return render(request, 'index.html', context)


def produtos(request):
	return render(request, 'products.html')
