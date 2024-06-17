from django import forms
from .models import Usuario, Avatar
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model=User
        field=["username", "password"]


class RegistroForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=150)
    email = forms.EmailField(label='Correo electrónico')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nombres', max_length=30)
    last_name = forms.CharField(label='Apellido', max_length=30)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["first_name", "last_name", "email"]
        widgets = {
            "password": forms.PasswordInput(),
        }


class PasswordForm:
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["nombre_de_imagen", "avatar_Main_Img"]
