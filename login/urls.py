from django.urls import path
from . import views 
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from login.views import CustomLoginView

app_name = "login"
urlpatterns = [
    path("iniciar/", CustomLoginView.as_view(), name="iniciar"),
    path("registro/", views.registro, name="registro"),
    path("salir/", views.salir, name="salir"),
    # """
    # usuario CRUD
    # """
    path("usuario/", views.usuario_detalle, name="usuario_detalle"),
    path("usuario/editar/", views.usuario_editar, name="usuario_editar"),
    path("usuario/password/", views.password_editar, name="password_editar"),
    path("image_upload", views.avatar_image_view, name="image_upload"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)