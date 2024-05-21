from django.urls import path
from . import views
app_name="login"

urlpatterns = [
    path("iniciar/", views.iniciar, name="iniciar"),
    path("registro/", views.registro, name="registro"),

]
