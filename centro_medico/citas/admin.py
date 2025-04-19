from django.contrib import admin
from .models import Cita


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'medico', 'fecha_cita', 'hora_cita', 'estado')
    search_fields = ('paciente__nombre_completo', 'medico__nombre_completo')
    list_filter = ('fecha_cita', 'hora_cita')
    ordering = ('-fecha_cita', '-hora_cita')

