from django.urls import path
from personas.views import home, exito

urlpatterns = [
  path('', home), # /personas
  path('exito', exito), # /personas/exito
]