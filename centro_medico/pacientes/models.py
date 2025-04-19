from django.db import models

class Paciente(models.Model):
    
    nombre_completo = models.CharField(max_length=150)
    dni = models.CharField(max_length=8, unique=True)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField(blank=True)
    numero_telefono = models.CharField(max_length=9)
    
    def __str__(self):
        return f"{self.nombre_completo} ({self.dni})"