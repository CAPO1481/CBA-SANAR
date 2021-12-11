from django.urls import path
from app.views import ingresar, index, regUsers, registrar, turnos1, asigTurnos, usuarios1

urlpatterns = [
    path('ingresar/', ingresar),
    path('index/', index),
    path('usuarios/', usuarios1),
    path('registro/', registrar),
    path('turnos/', turnos1),
    path('asignar/', asigTurnos),
]