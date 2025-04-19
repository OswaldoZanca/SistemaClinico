from django.db import models
from pacientes.models import Paciente
from medicos.models import Medico
from django.utils import timezone

class Cita(models.Model):
    ESTADOS_OPCIONES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    fecha_cita = models.DateField(default=timezone.now)
    hora_cita = models.TimeField()
    estado = models.CharField(
        max_length=10,
        choices=ESTADOS_OPCIONES,
        default='pendiente',
    )
    
    def __str__(self):
        return f"{self.fecha_cita} {self.hora_cita} - {self.paciente.nombre_completo} con {self.medico.nombre_completo}"