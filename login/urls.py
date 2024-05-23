from django.urls import path
from login import views
from django.contrib.auth.views import LogoutView

app_name = 'login'

urlpatterns = [
    path('signup/', views.registro, name='registro'),
    path('login/', views.iniciar, name='iniciar'),
    path('logout/', views.salir, name='logout'),
]
