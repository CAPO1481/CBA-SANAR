from django.urls import path
from .views import ingresar, index, usuarios, registro_usuarios, turnos, asignacion_turnos

urlpatterns = [
    path('ingresar/', ingresar, name='ingresar'),
    path('index/', index, name='index'),
    path('usuarios/', usuarios, name='usuarios'),
    path('registro_usuarios/', registro_usuarios, name='registro_usuarios'),
    path('turnos/', turnos, name='turnos'),
    path('asignacion_turnos/', asignacion_turnos, name='asignacion_turnos'),
]