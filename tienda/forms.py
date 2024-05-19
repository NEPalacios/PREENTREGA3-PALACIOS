from django import forms
from .models import Productos, Clientes

class PedidosForm(forms.Form):
    cliente = forms.ModelChoiceField(queryset=Clientes.objects.all(), label="Seleccione un Cliente")
    productos = forms.ModelMultipleChoiceField(queryset=Productos.objects.all(), label="Seleccione Productos")