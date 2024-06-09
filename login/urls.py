from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path("iniciar/", views.iniciar, name="iniciar"),
    path("registro/", views.registro, name="registro"),
    path("salir/", views.salir, name="salir"),
    # """
    # usuario CRUD
    # """
    path("usuario/", views.usuario_detalle, name="usuario_detalle"),
    path("usuario/editar/", views.usuario_editar, name="usuario_editar"),
    path("usuario/password/", views.password_editar, name="password_editar"),
]
