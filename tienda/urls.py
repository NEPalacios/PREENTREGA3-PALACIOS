
from django.contrib import admin
from django.urls import path
from tienda import views

app_name = "tienda"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    #mostrar todos los productos,alta
    path("productos/", views.consultar, name="consultar"),
    path("productos/guardar", views.guardar, name="guardar"),
    path("eliminar/<int:id>", views.eliminar, name="eliminar"),

    #mostrar los datos para actualizar
    path("detalle/<int:id>", views.detalle, name="detalle"),
    path("productos/editar/<int:id>", views.editar, name="editar"),
]
