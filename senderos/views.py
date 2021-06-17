from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core import serializers
import json
from django.forms.models import model_to_dict
from .models import *
import pickle
from django.contrib import messages
from .forms import SenderoForm


def saludo(request):
	return HttpResponse("Holaaa")


def senderos_home(request):
	senderos = Sendero.objects.all()[:10]
	context = {'senderos': senderos}
	print(repr(context))

	return render(request, 'home_cards_senderos.html', context)


def createSenderoFormular(request):
	context = {}
	context['form']=SenderoForm()
	return render(request, 'home_add_sendero.html', context)


def createSendero(request):

	print("Formulario")
	context = {}
	if request.method == 'POST':
		form = SenderoForm(request.POST)
		if form.is_valid():
			datos_formulario = form.cleaned_data
			nuevoSendero = Sendero(nombre=datos_formulario['nombre'],
						 descripcion=datos_formulario['descripcion'],
						 duracion=datos_formulario['duracion']
						 
			).save()
			nuevoSendero.fotos = [Foto(alt=datos_formulario['alt'], url=datos_formulario['url'])]
			nuevoSendero.save()
			messages.add_message(request, messages.INFO, 'Sendero añadido correctamente')
		
	return render(request, 'home_cards_senderos.html', context)

