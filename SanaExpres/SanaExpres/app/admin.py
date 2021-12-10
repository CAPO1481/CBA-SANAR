from django.contrib import admin
from .models import usuarios, turnos
# Register your models here.
class Usuario_admin(admin.ModelAdmin):
    list_display = ["Usuario", "Nombre", "Especialidad"]

admin.site.register(usuarios, Usuario_admin)
admin.site.register(turnos)