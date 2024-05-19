from django.contrib import admin
from tienda.models import Productos, Clientes, Pedidos


# Register your models here.
admin.site.register(Productos)

admin.site.register(Clientes)
admin.site.register(Pedidos)
