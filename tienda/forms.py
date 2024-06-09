from django import forms
from .models import Clientes, Productos


class PedidosForm(forms.Form):
    cliente = forms.ModelChoiceField(
        queryset=Clientes.objects.all(),
        label="Seleccione un Cliente",
        to_field_name="id",
    )
    productos = forms.ModelMultipleChoiceField(
        queryset=Productos.objects.all(),
        label="Seleccione Productos",
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        super(PedidosForm, self).__init__(*args, **kwargs)
        self.fields["cliente"].label_from_instance = self.get_cliente_label

    def get_cliente_label(self, cliente):
        return f"{cliente.id} - {cliente.nombre}"
