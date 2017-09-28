# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Evento


def home(request):
	eventos = Evento.objects.all().order_by('-data')[:5]
	context = {'agenda': eventos}
	if request.method == 'POST':
		email_usuario = request.POST.get('email')

		mensagem = 'Nome: %s\nEmail: %s\nMensagem: %s' % (request.POST.get('name'), email_usuario, request.POST.get('message'))
		assunto = request.POST.get('subject')		
		email = EmailMessage(assunto, mensagem, email_usuario, to=['jaquebelloni@gmail.com'], headers = {'Reply-To': email_usuario})
		email.send()

		messages.success(request, 'Seu contato foi enviado com sucesso! Clique no x para fechar esta mensagem.')
		return redirect(reverse('home'))

	return render(request, 'index.html', {'agendas': eventos})


def produtos(request):
	return render(request, 'products.html')


def eventos(request):
	eventos = Evento.objects.all().order_by('-data')
	return render(request, 'events.html', {'eventos': eventos})



