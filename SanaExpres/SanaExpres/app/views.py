from django.db import models
from django.shortcuts import render
from .models import usuarios
# Create your views here.

def base(request):
    return render(request, 'views/base.html')

def ingresar(request):
    return render(request, 'views/ingresar.html')

def index(request):
    return render(request, 'views/index.html')

def usuarios(request):
    usuario= usuarios.objects.all()
    data = {
        'usuario' : usuario
    }
    return render(request, 'views/usuarios.html', data)

def registro_usuarios(request):

    return render(request, 'views/registro_usuarios.html')

def turnos(request):
    return render(request, 'views/turnos.html')

def asignacion_turnos(request):
    return render(request, 'views/asignacion_turnos.html')