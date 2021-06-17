from mongoengine import *
from django.contrib.auth.models import User

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

uri = os.getenv('MONGO_URI',"noconnection")

db = mongoengine.connect(host=uri)

userpepe = User.objects.create_user('pepe', 'pepe@pepe.com', 'pepepassword')
user.save()