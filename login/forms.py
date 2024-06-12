from django import forms
from .models import Usuario, Avatar


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombres", "apellido"]
        widgets = {
            "password": forms.PasswordInput(),
        }


class PasswordForm:
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["nombre_de_imagen", "avatar_Main_Img"]
