from django.contrib import admin
from personas.models import Persona

class PersonaAdmin(admin.ModelAdmin):
  pass

admin.site.register(Persona, PersonaAdmin)
