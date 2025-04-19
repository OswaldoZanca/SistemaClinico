from django.db import models


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Medico(models.Model):
    nombre_completo = models.CharField(max_length=150)
    correo_electronico = models.EmailField(blank=True)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.PROTECT, related_name='medicos_especialidad')

    def __str__(self):
        return f"{self.nombre_completo} - {self.especialidad.nombre}"
