from mongoengine import connect, Document, EmbeddedDocument	
from mongoengine.fields import EmbeddedDocumentField, StringField, ListField, IntField, DateTimeField
from datetime import datetime
import sys
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

uri = os.getenv('MONGO_URI',"noconnection")





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


def crear_senderos():
	fotos = [
		{
			'alt': 'foto',
			'url': 'https://www.turgranada.es/wp-content/uploads/sites/2/2014/02/alhama-de-granada-1.jpg?x53512'
		}
	]

	comentarios = [
		{
			'resenia': 'Me parece una ruta impresionante',
			'autor': 'pepitoenpeligro'
		},
		{
			'resenia': 'Es muy cansada',
			'autor': 'stevejobs'
		}
	]

	sendero = Sendero(nombre="Alhama, la ciudad de los tajos",
				descripcion="Símbolo de la conquista cristiana del Reino de Granada, Alhama alberga joyas históricas junto al paraje conocido como Los Tajos. Para el poeta Teophile Gautier, la ciudad estaba “colgada de una enorme roca”. Esta maravilla geológica compite en belleza con edificios que son la huella de árabes y cristianos en el centro de la localidad como la Iglesia de la Encarnación.",
				likes=3,
				visitas=120,
				duracion=185, 
				tags=['cristiana', 'historia', 'media'], 
				comentarios=comentarios, 
				fotos=fotos)
	sendero.save()

	fotos = [
		{
			'alt': 'foto',
			'url': 'https://www.turgranada.es/wp-content/blogs.dir/2/files_mf/cache/th_db40546b061c7ee23bbbbcfbeb9d4806_fonfria2.jpg?x53512'
		}
	]

	comentarios = [
		{
			'resenia': 'Me encanta',
			'autor': 'pepitoenpeligro'
		},
		{
			'resenia': 'Me gusta, me encanta, pero cansa',
			'autor': 'cristinaortiz'
		}
	]

	sendero = Sendero(nombre="Barranco de La Fonfría y pino de La Señora",
				descripcion="El Parque Natural de la Sierra de Baza ofrece un refrescante recorrido por el arroyo de Baúl que permite contemplar uno de los mayores ejemplares de pino laricio de la provincia de Granada.",
				likes=1,
				visitas=65,
				duracion=250, 
				tags=['baza', 'arroyo', 'dificil'], 
				comentarios=comentarios, 
				fotos=fotos)

	sendero.save()




if __name__ == "__main__":
	db = connect(host=uri)
	crear_senderos()