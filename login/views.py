from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, PasswordForm, AvatarForm, RegistroForm
from .models import Usuario


def iniciar(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("tienda:index")
        return render(
            request,
            "login/iniciar.html",
            {"form": form, "error": "Nombre de usuario o contraseña incorrectos"},
        )
    else:
        form = AuthenticationForm()
        return render(request, "login/iniciar.html", {"form": form})


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            user = User.objects.create_user(username=username, email=email, password=password)
            user.nombre = nombre
            user.apellido = apellido
            user.save()
            return redirect('tienda:index')
    else:
        form = RegistroForm()
    
    return render(request, 'login/usuarioRegistro.html', {'form': form})
def salir(request):
    logout(request)
    return redirect("tienda:index")


@login_required
def usuario_detalle(request):
    usuario = request.user
    return render(request, "login/usuario.html", {"usuario": usuario})


@login_required
def usuario_editar(request):
    usuario = request.user 
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado con éxito")
            return redirect("login:usuario_detalle")
        else:
            messages.error(request, "Error al actualizar el perfil")
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, "login/usuarioEditar.html", {"form": form})


def password_editar(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            nueva_contraseña = form.cleaned_data["password"]
            usuario_actual = request.user
            usuario_actual.password = nueva_contraseña
            usuario_actual.save()
            return redirect("perfil")
    else:
        form = PasswordForm()
    return render(request, "login/password_editar.html", {"form": form})


def avatar_image_view(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("tienda:index")
    else:
        form = AvatarForm()
    return render(request, "login/avatar_image_upload.html", {"form": form})
