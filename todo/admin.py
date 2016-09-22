from django.contrib import admin
from .models import Especialidad, Paciente, Doctor, Consulta
# Register your models here.


@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']


class PacienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'cedula']
    search_fields = list_display

admin.site.register(Paciente, PacienteAdmin)


admin.site.register(Doctor)


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'paciente', 'hora', 'fecha']

