# from django import forms
from django.db import models
from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from mongoengine import *
import json


# Modelo Comentario
# @autor: string que define el nickname del usuario que ha hecho el comentario
# @resenia: string que define el valor del comentario en sí (reseña)
class Comentario(EmbeddedDocument):
	autor = StringField(required=True)
	resenia = StringField(required=True)

# Modelo Foto
# @alt: string que define la descripción de la imagen
# @url: string que define la ubicación de la foto (url)
class Foto(EmbeddedDocument):
	alt = StringField()
	url = StringField()

# Modelo Sendero
# @nombre: nombre del sendero
# @descripcion: descripcion del sendero
# @likes: numero de veces que ha gustado del sendero
# @visitas: numero de veces que se ha visitado del sendero
# @duracion: tiempo en segundos que dura del sendero
# @tags: vector de tags
# @comentarios: lista de comentarios asociadas a del sendero
# @fotos: lista de fotos
class Sendero(Document):
	nombre = StringField(max_length=80, required=True)
	descripcion = StringField(required=True)
	likes = IntField(default=0)
	visitas = IntField(default=0)
	duracion = IntField(default=0)
	tags = ListField(StringField(max_length=30))
	comentarios = ListField(EmbeddedDocumentField(Comentario))
	fotos = ListField(EmbeddedDocumentField(Foto))



class FotoSerializer(serializers.Serializer):
	alt = serializers.CharField(max_length=256)
	url = serializers.CharField(max_length=256)



class SenderoSerializer(serializers.Serializer):
	# Identificador único
	id = serializers.UUIDField(required=False)
	nombre = serializers.CharField(max_length=80)
	descripcion = serializers.CharField(max_length=1024)
	likes = serializers.IntegerField(default=0)
	duracion = serializers.IntegerField(default=0)
	visitas = serializers.IntegerField(default=0)
	fotos = serializers.ListField(child=FotoSerializer())

	def create(self, validated_data):
		print("CREANDO NUEVO SENDERO")
		print(validated_data)
		sendero = Sendero(nombre = validated_data['nombre'], descripcion=validated_data['descripcion'])

		if validated_data.get('fotos', None) is not None:

			print(validated_data)
			
			# Tomamos del mapa validated_data el campo foto y alt para crear el objeto foto
			sendero.fotos.append(Foto(url=validated_data['fotos'][0]['url'], alt=validated_data['fotos'][0]['alt']))
		else:
			sendero.fotos.append(Foto(url="https://www.fundaciocaixaltea.com/wp-content/uploads/2018/01/default-profile.png", alt=""))
			
		sendero.save()
		return sendero

	def update(self, sendero, validated_data):
		print("Updating")
		nombre = serializers.CharField(max_length=80)
		descripcion = serializers.CharField(max_length=1024)
		likes = serializers.IntegerField(default=0)
		duracion = serializers.IntegerField(default=0)
		visitas = serializers.IntegerField(default=0)
		fotos = serializers.ListField(child=FotoSerializer())
		sendero.nombre = validated_data['nombre']
		sendero.descripcion = validated_data['descripcion']
		sendero.likes = validated_data['likes']
		sendero.duracion = validated_data['duracion']
		sendero.visitas = validated_data['visitas']
		
		if validated_data.get('fotos', None) is not None:

			print(validated_data)
			
			# Tomamos del mapa validated_data el campo foto y alt para crear el objeto foto
			sendero.fotos.append(Foto(url=validated_data['fotos'][0]['url'], alt=validated_data['fotos'][0]['alt']))
		else:
			sendero.fotos.append(Foto(url="https://www.fundaciocaixaltea.com/wp-content/uploads/2018/01/default-profile.png", alt=""))

		# sendero.nombre = nombre
		# sender.descripcion = descripcion

		# if validated_data.get('fotos', None) is not None:

		# 	sendero.fotos.append(Foto(url=validated_data['url'], alt=validated_data['alt']))
		# else:
		# 	sendero.fotos.append(Foto(url=validated_data['url'], alt=""))
			
		sendero.save()
		return sendero