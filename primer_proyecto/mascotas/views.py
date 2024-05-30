from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.
def paginaMascotas(req):
  context = {
    'titulo': 'Esta es la Página de las Mascotas ;)',
    'esAdmin': True,
    'nombre': 'Carlos Toledo'
  }
  return render(req, 'mascotas.html', context)
