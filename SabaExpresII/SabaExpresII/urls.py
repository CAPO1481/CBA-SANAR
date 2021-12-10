from django.urls import path
from app.views import ingresar, index, regUsers, registar, turnos, asignacion_turnos, usuarios1

urlpatterns = [
    path('ingresar/', ingresar),
    path('index/', index),
    path('usuarios/', usuarios1),
    path('registro/', registar),
    path('turnos/', turnos),
    path('asignacion_turnos/', asignacion_turnos),
]