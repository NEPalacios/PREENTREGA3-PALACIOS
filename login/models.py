from django.db import models
from django import forms


class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.EmailField(max_length=100, blank=True, null= True)

    def __str__(self):
        return f"{self.nombres} {self.apellido}"


class PasswordForm(forms.Form):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class Avatar(models.Model):
    nombre_de_imagen = models.CharField(max_length=50)
    avatar_Main_Img = models.ImageField(upload_to="images/")
