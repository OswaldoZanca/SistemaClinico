from django.urls import path
from . import views

app_name = 'citas'

urlpatterns = [
    
    path('listar/', views.listado_citas, name = 'listado_citas'),
    path('crear/', views.crear_cita, name = 'crear_cita'),
    path('editar/<int:pk>/', views.editar_cita, name = 'editar_cita'),
    path('eliminar/<int:pk>/', views.eliminar_cita, name = 'eliminar_cita'),
]