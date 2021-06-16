# from django import forms
from django.db import models
from rest_framework import serializers
from django.core.validators import FileExtensionValidator
from mongoengine import *


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



