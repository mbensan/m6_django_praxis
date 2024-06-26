from django.shortcuts import redirect, render # type: ignore
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

def detalleMascota(req, id):
  id = int(id)
  mascota_buscada = None
  for masc in mascotas:
    if masc['id'] == id:
      mascota_buscada = masc
      break
  context = {
    'mascota': mascota_buscada
  }
  return render(req, 'detalle.html', context)

def crear_mascota (req):
  print(req.POST['nombre'])
  print(req.POST['especie'])
  nueva_mascota = {
    'nombre': req.POST['nombre'],
    'especie': req.POST['especie']
  }
  mascotas.append(nueva_mascota)
  return redirect('/pets')
