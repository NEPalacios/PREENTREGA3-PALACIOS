from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from .forms import UsuarioForm
from .models import Usuario

def iniciar(request):
    if request.method == "GET":
        return render(request, "login/iniciar.html", {"form": AuthenticationForm()})
    else:
        name = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=name, password=password)
        if user is None:
            return render(request, "login/iniciar.html", {"form": AuthenticationForm(), "error": "Nombre de usuario o contraseña incorrectos"})
        else:
            login(request, user)
            return redirect('tienda:index')

def registro(request):
    if request.method == "GET":
        return render(request, "login/registro.html", {"form": UserCreationForm()})
    else:
        if request.POST["password1"] != request.POST["password2"]:
            return render(
                request,
                "login/registro.html",
                {"form": UserCreationForm(), "error": "Las contraseñas no coinciden"},
            )
        else:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                Usuario.objects.create(
                    username=user.username,
                    nombres=request.POST.get("nombres", ""),
                    apellido=request.POST.get("apellido", "")
                )
                login(request, user)
                return redirect('tienda:index')
            except IntegrityError:
                return render(
                    request,
                    "login/registro.html",
                    {
                        "form": UserCreationForm(),
                        "error": "El nombre de usuario ya existe",
                    },
                )

def salir(request):
    logout(request)
    return redirect('tienda:index')

@login_required
def usuario_perfil(request):
    try:
        usuario = Usuario.objects.get(username=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None

    return render(request, 'login/usuario.html', {'usuario': usuario})

@login_required
def editar_usuario(request):
    try:
        usuario = Usuario.objects.get(username=request.user.username)
    except Usuario.DoesNotExist:
        usuario = None

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado con éxito')
            return redirect('login:usuario_perfil')
        else:
            messages.error(request, 'Error al actualizar el perfil')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'login/editarUsuario.html', {'form': form})
