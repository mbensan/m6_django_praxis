from django.http import HttpResponse
from django.shortcuts import render

from main.pasteles import pasteles

# Create your views here.
def indice(req):
  context = {'pasteles': pasteles}
  return render(req, 'index.html', context)
