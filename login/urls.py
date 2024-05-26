from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    path("iniciar/", views.iniciar, name="iniciar"),
    path("registro/", views.registro, name="registro"),
    path("salir/", views.salir, name="salir"),
    path("perfil/", views.usuario_perfil, name="usuario_perfil"),
    path("perfil/editar/", views.editar_usuario, name="editar_usuario"),
]
