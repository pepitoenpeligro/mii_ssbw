from __future__ import unicode_literals
from django.apps import AppConfig

class SenderosConfig(AppConfig):
    name = 'senderos'

    def ready(self):
        print("La aplicacion de senderos esta lista")
        import senderos.signals