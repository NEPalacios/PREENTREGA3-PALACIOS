from django.urls import path
from .views import registro, iniciar
from django.contrib.auth.views import LogoutView

app_name = 'login'

urlpatterns = [
    path('signup/', registro, name='registro'),
    path('login/', iniciar, name='iniciar'),
    path('logout/', LogoutView.as_view(next_page='login:iniciar'), name='logout'),
]
