from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellido']
        widgets = {
            'password': forms.PasswordInput(),
        }
