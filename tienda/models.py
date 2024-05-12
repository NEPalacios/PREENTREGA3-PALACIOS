from django.db import models


# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


# class Pedido(models.Model):
#     cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#     fecha_pedido = models.DateField()
#     total = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Pedido de {self.cliente} - {self.fecha_pedido}"