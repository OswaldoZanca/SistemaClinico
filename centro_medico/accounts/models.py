from django.db import models
from django.contrib.auth.models import User 

class PerfilUsuario(models.Model):
    ROLES_OPCIONES = [
        ('admin', 'Administrador'),
        ('recepcionista', 'Recepcionista'),
        ('medico', 'Médico'),
    ]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.CharField(max_length=20, choices=ROLES_OPCIONES)
    esta_activo = models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"{self.usuario.username} - {self.rol}"
