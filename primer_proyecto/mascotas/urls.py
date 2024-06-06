from django.urls import path
from mascotas.views import crear_mascota, paginaMascotas, detalleMascota

urlpatterns = [
  path('', paginaMascotas), # /pets
  path('home/', paginaMascotas), # /pets/home
  path('<id>/', detalleMascota), # /pets/5
  path('create', crear_mascota)  # /pets/create
]