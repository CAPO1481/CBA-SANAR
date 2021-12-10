from django.db import models

# Create your models here.
class usuarios(models.Model):
    Nombre = models.CharField(max_length=50)
    Usuario = models.CharField(max_length=15)
    Celular = models.CharField(max_length=15)
    Correo = models.CharField(max_length=30)
    Especialidad = models.CharField (max_length=20)

    def __str__(self):
        return self.Usuario

class turnos (models.Model):
    Servicio = models.CharField(max_length=30)
    Especialidad = models.CharField(max_length=30)
    Empleado = models.ForeignKey(usuarios, on_delete=models.PROTECT)
    Fecha_inicio = models.DateField()
    Fecha_fin = models.DateField()
    Horario_inicio = models.TimeField()
    Horario_fin = models.TimeField()
    Descanso = models.CharField(max_length=30)

    def __str__(self):
        return self.Empleado