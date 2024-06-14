import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):
  uuid = models.UUIDField(editable=False,  default=uuid.uuid4)
  nombre = models.CharField(max_length=64)
  descripcion = models.TextField()
  precio = models.IntegerField(default=1000)
  imagen_url = models.URLField()
  is_private = models.BooleanField(default=False)

  def __str__(self) -> str:
    return self.nombre
  
class MiUsuario(User):

  def __init__(self, *args, **kwargs):
    super(args, kwargs)
    self.rut = models.CharField(max_length=12)


