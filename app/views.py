from django.shortcuts import render
from app.models import usuarios, turnos

def base(request):
    return render(request, 'views/base.html')

def ingresar(request):
    return render(request, 'views/ingresar.html')


def index(request):
    return render(request, 'views/index.html')

def usuarios1(request):
    usuario = usuarios.objects.all()
    if request.method == "POST": 
        if request.POST["Usuario"] and request.POST["Nombre"] and request.POST["Especialidad"]:
            usuario = usuarios.objects.filter(Usuario = request.POST["Usuario"], Nombre = request.POST["Nombre"], Especialidad = request.POST["Especialidad"])
        else:
            if request.POST["Usuario"] and request.POST["Nombre"]:
                usuario = usuarios.objects.filter(Usuario = request.POST["Usuario"], Nombre = request.POST["Nombre"])
            else:
                if request.POST["Usuario"]:
                    usuario = usuarios.objects.filter(Usuario = request.POST["Usuario"])
    data = {
        'usuario' : usuario
    }
    return render(request, 'views/verUsuarios.html', data)

def regUsers(request):
    #return render(request, 'views\regUsers.html')
    return render(request, 'views/regUsuarios.html')

def turnos1(request):
    turno = turnos.objects.all()
    if request.method == "POST": 
        asignacion = turnos.objects.filter(Servicio = request.POST["Servicio"], Empleado = request.POST["Empleado"], Especialidad = request.POST["Especialidad"], Fecha_inicio = request.POST["Fecha_inicio"], Fecha_fin = request.POST["Fecha_fin"])
    
    data = {
        'turnos' : turno
    }
    return render(request, 'views/turnos.html', data)

def asigTurnos(request):
    if request.method == "POST":
        asignacion = turnos.objects.create(Servicio = request.POST["Servicio"], Especialidad = request.POST["Especialidad"], Empleado = request.POST["Empleado"], Fecha_inicio = request.POST["Fecha_inicio"], Fecha_fin = request.POST["Fecha_fin"], Horario_inicio = request.POST["Horario_inicio"], Horario_fin = request.POST["Horario_fin"], Descanso = request.POST["Descanso"])
        
    usuario = usuarios.objects.all()  
    data = {
        'usuario' : usuario
    }
    return render(request,'views/asignacion_turnos.html', data)

def registrar(request):
    if request.method == "POST":
        registro = usuarios.objects.create(Nombre = request.POST["Nombre"], Usuario = request.POST["Usuario"], Celular = request.POST["Celular"], Correo = request.POST["Correo"], Especialidad = request.POST["Especialidad"])
    return render(request, 'views/regUsuarios.html')
