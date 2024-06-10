from django.db import models
from django import forms


class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombres} {self.apellido}"


class PasswordForm(forms.Form):
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class Avatar(models.Model):
    name = models.CharField(max_length=50)
    avatar_Main_Img = models.ImageField(upload_to="images/")
