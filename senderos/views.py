from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def saludo(request):
	return HttpResponse("Holaaa")


def senderos_home(request):
	# request.GET["clave"] <- pasando parametros por url
	
	# Post
	# if request.method == 'POST':
	#   form = Sendero(request.POST)
	#   if form.is_valid():
	#       
	
	senderos = Sendero.objects.all()[:4]
	context = {'senderos': senderos}
	print(context)
	return render(request, 'index.html', context)