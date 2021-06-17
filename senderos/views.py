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

def editar(request, id):
	# @todo Mejorar el paso de fotos, si no hubiera fotos, 
	# intentaria acceder al indice cero, qeu lo mismo ni existe
	context = {}
	context['id']=id
	form = SenderoForm()
	sendero = Sendero.objects.get(id=id)
	form = SenderoForm({'nombre': sendero.nombre,
						'descripcion': sendero.descripcion,
						'duracion': sendero.duracion,
						'url': sendero.fotos[0].url,
						'alt': sendero.fotos[0].alt
						})
	context = {
		'form': form,
		'sendero': sendero
	}
	return render(request, 'home_edit_sendero.html', context)


def editSenderoForm(request, id):
	context = {}
	
	if request.method == 'POST':
		form = SenderoForm(request.POST)
		if form.is_valid():
			print("Vamos a modificar un sendero")
			print(str(form.cleaned_data))
			datos_formulario = form.cleaned_data
			sendero = Sendero.objects.get(id=id)
			sendero.nombre=datos_formulario['nombre']
			sendero.descripcion=datos_formulario['descripcion']
			sendero.duracion=datos_formulario['duracion']
			sendero.save()
			sendero.fotos = [Foto(alt=datos_formulario['alt'], url=datos_formulario['url'])]
			sendero.save()
			messages.add_message(request, messages.INFO, 'Sendero modificado correctamente')
		
	return  redirect('/senderos')