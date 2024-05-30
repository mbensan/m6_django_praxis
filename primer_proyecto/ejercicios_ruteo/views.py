from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
# /blogs
def index(req):
  return render(req, 'blogs.html')

# /
def root(req):
  return redirect('/blogs')

# /blogs/json
def yeison(req):
  return JsonResponse({
    'blog1': 'Un blog para viajeros',
    'blog2': 'Un blog de cocina',
    'blog3': 'Un blog de viajeros que cocinan'
  }) 

