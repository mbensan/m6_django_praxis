from django.http import HttpResponse
from django.shortcuts import render

from main.pasteles import pasteles

# Create your views here.
def indice(req):
  return render(req, 'index.html', {})
