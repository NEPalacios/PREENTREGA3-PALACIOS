from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombres', 'apellido']
        widgets = {
            'password': forms.PasswordInput(),
        }

class PasswordForm():
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)