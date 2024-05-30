from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

# Create your views here.
mascotas = [
  {'id': 1,
   'nombre': 'Pelusa',
   'especie': 'gato',
   'vacunas': ['octuple']},
  {'id': 2,
   'nombre': 'Rocky',
   'especie': 'perro',
   'vacunas': ['octuple', 'antirrabica']},
  {'id': 3,
   'nombre': 'Nemo',
   'especie': 'pez',
   'vacunas': ['antibioticos', 'melipass']},
]

def paginaMascotas(req):
  context = {
    'titulo': 'Esta es la Página de las Mascotas ;)',
    'esAdmin': False,
    'nombre': 'Carlos Toledo',
    'mascotas': mascotas
  }
  return render(req, 'mascotas.html', context)
