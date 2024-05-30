from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hola(req):
  return HttpResponse('Hola curso!!')

def chao(req):
  return HttpResponse('<h1>Chao Pescao!!</h1>')

def saludar(req, nombre):
  return HttpResponse(f'<h3>Hola {nombre}</h3>')

def poliglota(req, nombre, idioma):
  # saluda a la persona dependiendo del idioma ingresado
  
  return HttpResponse('No entiendo ese idioma')