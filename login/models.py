from django.db import models


class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.nombres} {self.apellido}'


