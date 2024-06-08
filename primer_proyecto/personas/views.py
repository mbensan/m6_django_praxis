from django.http import HttpResponse
from django.shortcuts import redirect, render
from personas.forms import PersonaForm
from personas.models import Persona

# Create your views here.
def home(req):
  if req.method == 'GET':
    form = PersonaForm()
    context = {'form': form}
    return render(req, 'personas.html', context)
    # renderizamos la página
  else:
    # validamos el formulario
    form = PersonaForm(req.POST)
    if form.is_valid():
      # Esta es la forma de pedirle a un modelo que cree un registro usando los datos de un formulario
      Persona.objects.create(
        **form.cleaned_data
      )
      return redirect('/personas/exito')
    context = {'form': form}
    return render(req, 'personas.html', context)

def exito(req):
  return HttpResponse('Eeeexito!!!!')