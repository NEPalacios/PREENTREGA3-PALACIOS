from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

def iniciar(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tienda:index')  # Redirige a la página de inicio después de iniciar sesión
        else:
            return render(request, "login/iniciar.html", {"error": "Nombre de usuario o contraseña incorrectos"})
    else:
        return render(request, "login/iniciar.html")

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
                    password=request.POST["password1"]
                )
                user.save()
                login(request, user)  # Inicia sesión automáticamente al usuario después de registrarse
                return redirect('tienda:index')  # Redirige a la página de inicio después del registro
            except IntegrityError:
                return render(
                    request,
                    "login/registro.html",
                    {"form": UserCreationForm(), "error": "El nombre de usuario ya existe"},
                )
