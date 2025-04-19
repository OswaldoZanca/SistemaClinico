from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita
from .forms import CitaForms  # Import CitaForm from the forms module


def listado_citas(request):
    citas = Cita.objects.select_related('paciente', 'medico').all
    return render(request, 'citas/listado_citas.html', {'citas':citas})

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citas:listado_citas')
    else:
        form = CitaForms()
    return render(request, 'citas/form_cita.html', {'form': form, 'accion': 'Registrar'})

def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForms(request.POSTm, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('listado_citas')
    else:
        form = CitaForms(instance = cita)
    return render(request, 'citas/form_cita.html', {'form': form, 'accion': 'Editar'})

def eliminar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('listado_citas')
    return render(request, 'citas/confirm_delete.html', {'cita': cita})