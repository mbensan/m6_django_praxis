from django.urls import path
from ejercicios_ruteo.views import index, root, yeison

urlpatterns = [
  path('', root),
  path('blogs/', index),
  path('blogs/json', yeison),
  # path('/blogs/create'),
  # path('/blogs/<number: int>')
]