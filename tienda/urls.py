from django.contrib import admin
from django.urls import path
from tienda import views

app_name = "tienda"

urlpatterns = [
    path("admin/", admin.site.urls),
    #pagina de inicio- todavia vacia
    path("", views.index, name="index"),

    # mostrar todos los productos,alta
    path("productos/", views.consultar, name="consultar"),
    path("productos/guardar", views.guardar, name="guardar"),
    path("eliminar/<int:id>", views.eliminar, name="eliminar"),
    # mostrar los datos para actualizar
    path("detalle/<int:id>", views.detalle, name="detalle"),
    path("productos/editar/<int:id>", views.editar, name="editar"),

#############################################

    # cliente cliente cliente CRUD
    path("cliente/", views.cliente_consultar, name="cliente_consultar"),
    path('cliente/guardar', views.cliente_create, name='cliente_create'),
    path('cliente_eliminar/<int:id>', views.cliente_eliminar,name="cliente_eliminar"),
    # mostrar los datos para actualizar
    path("cliente_detalle/<int:id>", views.cliente_detalle, name="cliente_detalle"),
    path("cliente/editar/<int:id>", views.cliente_editar, name="cliente_editar"),
]
