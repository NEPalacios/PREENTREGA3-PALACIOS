from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .forms import UsuarioForm, PasswordForm, AvatarForm
from .models import Usuario
from django.http import HttpResponse


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
def usuario_detalle(request):
    usuario = request.user
    return render(request, 'login/usuario.html', {'usuario': usuario})

@login_required
def usuario_editar(request):
    try:
        usuario = Usuario.objects.get(username=request.user.username)
        print(request)
        # print(usuario)
    except Usuario.DoesNotExist:
        usuario = None

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado con éxito')
            return redirect('login:usuario_detalle')
        else:
            messages.error(request, 'Error al actualizar el perfil')
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'login/editarUsuario.html', {'form': form})

def password_editar(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            nueva_contraseña = form.cleaned_data['password']
            usuario_actual = request.user
            usuario_actual.password = nueva_contraseña
            usuario_actual.save()
            return redirect('perfil')
    else:
        form = PasswordForm()
    return render(request, 'login/password_editar.html', {'form': form})

def avatar_image_view(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tienda:index')
    else:
        form = AvatarForm()
    return render(request, 'login/avatar_image_upload.html', {'form': form})
