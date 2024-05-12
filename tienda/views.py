from django.shortcuts import render, redirect
from tienda.models import Producto
from django.contrib import messages

# Create your views here.


# AGREGAR ""SIEMPRE"" :      CARPETA / HTML
def index(request):
    return render(request, "tienda/index.html")


def consultar(request):
    #buscador y mostrar toda la base de datos
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        productos = Producto.objects.filter(nombre__icontains = busqueda)
    else:
        productos = Producto.objects.all()
    return render(request, "tienda/productos.html", {"productos": productos})


def guardar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    # para crear el producto
    # modelo = variable
    p = Producto(nombre=nombre, precio=precio, descripcion=descripcion)
    p.save()
    # agregar el mensaje
    messages.success(request, "Producto agregado")
    # para redirigir a la vista 'consultar'
    return redirect("tienda:consultar")


def eliminar(request, id):
    producto = Producto.objects.filter(pk=id)
    producto.delete()
    messages.success(request, "Producto eliminado")
    return redirect("tienda:consultar")


# mostrar en detalles y modificar un producto
def detalle(request, id):
    producto = Producto.objects.get(pk=id)
    return render(request, "tienda/productoEditar.html", {"producto": producto})


def editar(request, id):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    # campo oculto en el formulario editar
    id = request.POST['id']
    Producto.objects.filter(pk=id).update(
        nombre=nombre, precio=precio, descripcion=descripcion
    )
    messages.success(request, "Producto actualizado")
    return redirect("tienda:consultar")