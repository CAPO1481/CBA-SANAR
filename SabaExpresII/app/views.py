from django.shortcuts import render
from app.models import usuarios

def base(request):
    return render(request, 'views\base.html')

def ingresar(request):
    return render(request, 'views\ingresar.html')


def index(request):
    return render(request, 'views\index.html')

def usuarios1(request):
    usuario= usuarios.objects.all()
    if request.method == "POST": 
        usuario = usuarios.objects.filter(Nombre = request.POST["Nombre"])
    data = {
        'usuario' : usuario
    }
    return render(request, 'views\VerUsuarios.html', data)

def regUsers(request):
    #return render(request, 'views\regUsers.html')
    return render(request, 'views\regUsers.html')

def turnos(request):
    return render(request, 'views/turnos.html')

def asignacion_turnos(request):
    return render(request, 'views/asignacion_turnos.html')

def registar(request):
    if request.method == "POST":
        registro = usuarios.objects.create(Nombre = request.POST["Nombre"], Usuario = request.POST["Usuario"], Celular = request.POST["Celular"], Correo = request.POST["Correo"], Especialidad = request.POST["Especialidad"])
    return render(request,'views/regUsers.html')
