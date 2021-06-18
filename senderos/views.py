from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core import serializers
import json
from django.forms.models import model_to_dict
from .models import *
import pickle
from django.contrib import messages
from .forms import SenderoForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from rest_framework.response import Response
from .models import *
from django.http import Http404, JsonResponse
from rest_framework.parsers import JSONParser

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from rest_framework import status




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
		if form.is_valid() and request.user.is_authenticated and  request.user.is_staff:
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
		if form.is_valid() and request.user.is_authenticated and  request.user.is_staff:
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
			messages.add_message(request, messages.INFO, 'Sendero modificado')
		
	return  redirect('/senderos')


def eliminar(request, id):
	if request.user.is_authenticated and  request.user.is_staff:
		context = {}
		print("Eliminando el sendero con id: %s" % (id))
		sendero = Sendero.objects.get(id=id)
		sendero.delete()
		messages.add_message(request, messages.INFO, 'Sendero eliminado')

	return  redirect('/senderos')


def createuser(request):
	# Es superuser
	User.objects.create_user('pepe', 'pepe@pepe.com', '201196', is_staff=True, first_name="Pepe", last_name="Córdoba")
	User.objects.create_user('juan', 'juan@juan.com', '201196', is_staff=False, first_name="Juan", last_name="Álava")
	return  redirect('/senderos')



def login(request):
	context = {}
	context['form']=LoginForm()
	print("Vas a loguear y tengo qeu renderizar otra pagina")
	return render(request, 'registration/login.html', context)
	# return  redirect('/senderos')


def dologin(request):
	print("dologin")
	context = {}
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			datos_formulario = form.cleaned_data
			# datos_formulario['nombre'],
			usuario = User.objects.get(username=datos_formulario['username'])
			user2 = authenticate(
				username=datos_formulario['username'],
				password=datos_formulario['password']
			)
			print(user2)
			auth_login(request, user2)
			if usuario.check_password(datos_formulario['password']) is True:
				print("El usuario es %s" % (usuario))
				request.session["user"] = usuario.id
			else:
				print("El usuario no fue encontrado")

	return  redirect('/senderos')

def dologout(request):
	context = {}
	logout(request)
	return  redirect('/senderos')


# path('api/senderos', getsenderos, name="getsenderos")
# def getsenderos(request):
# 	context = {}
# 	senderos = Sendero.objects.all()
# 	serial = SenderoSerializer(senderos, many=True)
# 	return JsonResponse({'senderos': serial.data}, json_dumps_params={'ensure_ascii': False})

# path('api/sendero/<str:id>', getsendero, name="getsendero"),		 
# def getsendero(request, id):
# 	context = {}
# 	sendero = Sendero.objects.get(id=id)
# 	print("Sendero: %s" % sendero)
# 	#data = JSONParser().parse(sendero)
# 	serial = SenderoSerializer(sendero)
# 	return JsonResponse({'sendero': serial.data}, json_dumps_params={'ensure_ascii': False})



class SenderoApi(APIView):
	# permission_classes = (IsAuthenticatedOrReadOnly,)
	def get(self, request, id):
		sendero = Sendero.objects.get(id=id)
		print("Sendero: %s" % sendero)
		#data = JSONParser().parse(sendero)
		serial = SenderoSerializer(sendero)
		return JsonResponse({'sendero': serial.data}, json_dumps_params={'ensure_ascii': False})
	
	def put(self, request, id):
		try:
			sendero = Sendero.objects.get(id=id)
			print("Encontre el sendero %s" % sendero)
			print("Datos %s" % request.data)
			serializer = SenderoSerializer(sendero, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except:
			raise Http404

	def delete(self, request, id):
		try:
			sendero = Sendero.objects.get(id=id)
			sendero.delete()
			serializer = SenderoSerializer(sendero)
			return Response(status=status.HTTP_202_ACCEPTED)
		except:
			raise Http404


class SenderosApi(APIView):
	# "detail": "Authentication credentials were not provided."
	# permission_classes = (IsAuthenticatedOrReadOnly,)
	def get(self, request):
		senderos = Sendero.objects.all()
		serial = SenderoSerializer(senderos, many=True)
		return JsonResponse({'senderos': serial.data}, json_dumps_params={'ensure_ascii': False})

	def post(self, request):
		serial = SenderoSerializer(data=request.data)
		if serial.is_valid():
			serial.save()
			return Response(serial.data, status=status.HTTP_201_CREATED)
		return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

	# def post(self, request):
	# 	serializer = ExcursionSerializer(data=request.data)

	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return Response(serializer.data, status=status.HTTP_201_CREATED)
	# 	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def addlike(request, id):
	sendero= Sendero.objects.get(id=id)
	sendero.likes = sendero.likes+1
	sendero.save()
	return JsonResponse({"likes": sendero.likes}, status=202)

def substractlike(request, id):
	sendero= Sendero.objects.get(id=id)
	sendero.likes = sendero.likes-1
	sendero.save()
	return JsonResponse({"likes": sendero.likes}, status=202)