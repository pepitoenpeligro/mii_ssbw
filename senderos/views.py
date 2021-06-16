from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
    return HttpResponse("Holaaa")


def senderos_home(request):
    context = {}
    return render(request, 'index.html', context)