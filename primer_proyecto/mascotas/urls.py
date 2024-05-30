from django.urls import path
from mascotas.views import paginaMascotas

urlpatterns = [
  path('', paginaMascotas)
]