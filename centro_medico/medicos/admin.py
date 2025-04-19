from django.contrib import admin
from .models import Medico, Especialidad


@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'correo_electronico', 'especialidad')
    search_fields = ('nombre_completo', 'correo_electronico','especialidad__nombre')
    ordering = ('nombre_completo',)
    list_filter = ('especialidad',)

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('nombre',)
    list_filter = ('nombre',)