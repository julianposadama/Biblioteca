from django.contrib import admin
from Proyecto.Apps.GestionBiblioteca.models import *

# Register your models here.

admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Libro)
admin.site.register(Prestamos)