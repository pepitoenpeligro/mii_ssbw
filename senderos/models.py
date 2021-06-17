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
	alt = StringField(required=True)
	url = StringField(required=True)

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


	

	




class SenderoSerializer(serializers.Serializer):
	# Identificador único
	id = serializers.UUIDField()
	nombre = serializers.CharField(max_length=80)
	descripcion = serializers.CharField(max_length=1024)
	likes = serializers.IntegerField(default=0)
	url = serializers.CharField(max_length=128)

	def create(self, validated_data):
		sendero = Sendero(nombre = validated_data['nombre'], descripcion=validated_data['descripcion']).save()

		if validated_data.get('foto', None) is not None:
			if validated_data.get('pie', None) is not None:
				# Tomamos del mapa validated_data el campo foto y alt para crear el objeto foto
				sendero.foto.append(Foto(url=validated_data['foto'], alt=validated_data['alt']))
			else:
				sendero.foto.append(Foto(url=validated_data['foto'], alt=None))
			
		sendero.save()
		return sendero

	def update(self, sendero, validated_data):
		sendero.nombre = validated_data['nombre']
		sendero.descripcion = validated_data['descripcion']

		if validated_data.get('foto', None) is not None:
			if validated_data.get('pie', None) is not None:
				sendero.foto.append(Foto(url=validated_data['url'], alt=validated_data['alt']))
			else:
				sendero.foto.append(Foto(url=validated_data['url'], alt=None))
			
		sendero.save()
		return sendero