from django import forms
from .models import Cita

class CitaForms(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'medico', 'fecha_cita', 'hora_cita', 'estado']
        