from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
import json
from django.forms.models import model_to_dict
from .models import *
import pickle


def saludo(request):
	return HttpResponse("Holaaa")


def senderos_home(request):
	# request.GET["clave"] <- pasando parametros por url
	
	# Post
	# if request.method == 'POST':
	#   form = Sendero(request.POST)
	#   if form.is_valid():
	#       
	
	senderos = Sendero.objects.all()[:10]
	context = {'senderos': senderos}
	print(repr(context))

	return render(request, 'index.html', context)