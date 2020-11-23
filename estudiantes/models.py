from django.db import models


class Estudiante(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    enrollment = models.IntegerField(null=True)
    sex = models.CharField(max_length=15)

    def __str__(self):
        return self.name
