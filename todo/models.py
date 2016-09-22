from __future__ import unicode_literals

from django.db import models

# Create your models here.


class BasePersona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=50, unique=True)

    class Meta:
        abstract = True
        unique_together = ['nombre', 'apellido', 'cedula']

    def __unicode__(self):
        return "{0} {1}".format(self.nombre, self.apellido)


class Paciente(BasePersona):
    pass


class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Especialidad'
        verbose_name_plural = 'Especialidades'

    def __unicode__(self):
        return self.nombre


class Doctor(BasePersona):
    especialidad = models.ForeignKey(Especialidad)

    def __unicode__(self):
        return '{0} {1} - especialidad : {2}'.format(self.nombre, self.apellido, self.especialidad)


class Consulta(models.Model):
    doctor = models.ForeignKey(Doctor)
    paciente = models.ForeignKey(Paciente)
    hora = models.TimeField()
    fecha = models.DateField()

    class Meta:
        unique_together = ['doctor', 'paciente', 'fecha', 'hora']
