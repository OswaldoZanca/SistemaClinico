from django.contrib import admin
from .models import PerfilUsuario

@admin.register(PerfilUsuario)
class PerfilUsuarioAmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'rol', 'esta_activo')
    search_fields = ('usuario__usarname', 'rol')
    list_filter = ('rol', 'esta_activo')
    ordering = ('usuario__username',)
