from django.contrib import admin
from django.urls import path
from tienda import views

app_name = "tienda"

urlpatterns = [
    path("admin/", admin.site.urls),
    # pagina de inicio- todavia vacia
    path("", views.index, name="index"),
    # mostrar todos los productos,alta
    path("productos/", views.productos_consultar, name="productos_consultar"),
    path("productos/guardar", views.productos_guardar, name="productos_guardar"),
    path("eliminar/<int:id>", views.productos_eliminar, name="productos_eliminar"),
    # mostrar los datos para actualizar
    path("productos_detalle/<int:id>", views.productos_detalle, name="productos_detalle"),
    path("productos/editar/<int:id>", views.productos_editar, name="productos_editar"),
    #############################################
    # cliente cliente cliente CRUD
    path("cliente/", views.cliente_consultar, name="cliente_consultar"),
    path("cliente/guardar", views.cliente_create, name="cliente_create"),
    path("cliente_eliminar/<int:id>", views.cliente_eliminar, name="cliente_eliminar"),
    # mostrar los datos para actualizar
    path("cliente_detalle/<int:id>", views.cliente_detalle, name="cliente_detalle"),
    path("cliente/editar/<int:id>", views.cliente_editar, name="cliente_editar"),
    #############################################
    # pedidos pedidos pedidos CRUD
    path("pedidos/", views.pedidos_consultar, name="pedidos_consultar"),
    path("pedidos/guardar", views.pedidos_create, name="pedidos_create"),
    path("pedidos_eliminar/<int:id>", views.pedidos_eliminar, name="pedidos_eliminar"),
    # mostrar los datos para actualizar
    path("pedidos_detalle/<int:id>", views.pedidos_detalle, name="pedidos_detalle"),
    path("pedidos/editar/<int:id>", views.pedidos_editar, name="pedidos_editar"),
]
