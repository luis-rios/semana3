from django.db import models

from estudiantes.models import Estudiante


class Clase(models.Model):
    name = models.CharField(max_length=200)
    schedule = models.DateTimeField()

    estudiantes = models.ManyToManyField(Estudiante, related_name='estudiante')

    def __str__(self):
        return self.name
