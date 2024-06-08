from django.db import models

# Create your models here.
class Persona(models.Model):
  nombre = models.CharField(max_length=15)
  email = models.CharField(max_length=15)
  edad = models.IntegerField(null=False)

