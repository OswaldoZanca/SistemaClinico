from django.contrib import admin
from .models import Paciente



@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'dni', 'fecha_nacimiento', 'correo_electronico', 'numero_telefono')
    search_fields = ('nombre_completo', 'dni', 'correo_electronico')
    ordering = ('nombre_completo',)
    list_filter = ('fecha_nacimiento',)
