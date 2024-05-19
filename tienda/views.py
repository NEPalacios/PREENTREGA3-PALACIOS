from django.shortcuts import render, redirect, get_object_or_404
from tienda.models import Productos, Clientes, Pedidos
from django.contrib import messages

from .forms import PedidosForm

# Create your views here.


# AGREGAR ""SIEMPRE"" : render(CARPETA / HTML)
def index(request):
    return render(request, "tienda/index.html")


def productos_consultar(request):
    # buscador y mostrar toda la base de datos
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        productos = Productos.objects.filter(nombre__icontains=busqueda)
    else:
        productos = Productos.objects.all()
    return render(request, "tienda/productos.html", {"productos": productos})


def productos_guardar(request):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    # para crear el producto
    # modelo = variable
    producto = Productos(nombre=nombre, precio=precio, descripcion=descripcion)
    producto.save()
    # agregar el mensaje
    messages.success(request, "Producto agregado")
    # para redirigir a la vista 'consultar'
    return redirect("tienda:productos_consultar")


def productos_eliminar(request, id):
    producto = Productos.objects.filter(pk=id)
    producto.delete()
    messages.success(request, "Producto eliminado")
    return redirect("tienda:productos_consultar")


# mostrar en detalles y modificar un producto
def productos_detalle(request, id):
    producto = Productos.objects.get(pk=id)
    return render(request, "tienda/productoEditar.html", {"producto": producto})


def productos_editar(request, id):
    nombre = request.POST["nombre"]
    precio = request.POST["precio"]
    descripcion = request.POST["descripcion"]
    # campo oculto en el formulario editar
    id = request.POST["id"]
    Productos.objects.filter(pk=id).update(
        nombre=nombre, precio=precio, descripcion=descripcion
    )
    messages.success(request, "Producto actualizado")
    return redirect("tienda:productos_consultar")


"""
CLIENTE CLIENTE CLIENTE CLIENTE CLIENTE CLIENTE 
"""


def cliente_consultar(request):
    # buscador y mostrar toda la base de datos
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        clientes = Clientes.objects.filter(nombre__icontains=busqueda)
    else:
        clientes = Clientes.objects.all()
    return render(request, "tienda/cliente.html", {"clientes": clientes})


def cliente_create(request):  # guardar
    # if request.method == "POST":
    nombre = request.POST["nombre"]
    email = request.POST["email"]
    telefono = request.POST["telefono"]
    cliente = Clientes(nombre=nombre, email=email, telefono=telefono)
    cliente.save()
    messages.success(request, "Cliente agregado")
    # Redirigir a la vista de lista clientes
    return redirect("tienda:cliente_consultar")


def cliente_eliminar(request, id):
    cliente = Clientes.objects.filter(pk=id)
    cliente.delete()
    messages.success(request, "Cliente eliminado")
    return redirect("tienda:cliente_consultar")


# mostrar en detalles y modificar un cliente
def cliente_detalle(request, id):
    cliente = Clientes.objects.get(pk=id)
    return render(request, "tienda/clienteEditar.html", {"cliente": cliente})


def cliente_editar(request, id):
    nombre = request.POST["nombre"]
    email = request.POST["email"]
    telefono = request.POST["telefono"]
    # campo oculto en el formulario editar
    id = request.POST["id"]
    Clientes.objects.filter(pk=id).update(nombre=nombre, email=email, telefono=telefono)
    messages.success(request, "Cliente actualizado")
    return redirect("tienda:cliente_consultar")


# PEDIDOS PEDIDOS PEDIDOS


def pedidos_consultar(request):
    pedidos = Pedidos.objects.all()
    form = PedidosForm()
    return render(request, "tienda/pedidos.html", {"pedidos": pedidos})


def pedidos_create(request):
    if request.method == "POST":
        form = PedidosForm(request.POST)
        if form.is_valid():
            form_cliente = form.cleaned_data["cliente"]
            form_productos = form.cleaned_data["productos"]
            pedido = Pedidos(cliente=form_cliente)
            pedido.save()
            pedido.productos.set(form_productos)
            pedido.save()
            messages.success(request, "El pedido se ha guardado exitosamente.")
            return redirect("tienda:pedidos_consultar")
    else:
        form = PedidosForm()
    return render(request, "tienda/pedidos.html", {"form": form})


def pedidos_eliminar(request, id):
    pedido = get_object_or_404(Pedidos, pk=id)
    pedido.delete()
    messages.success(request, "Pedido eliminado")
    return redirect("tienda:pedidos_consultar")


def pedidos_detalle(request, id):
    pedido = get_object_or_404(Pedidos, pk=id)
    form = PedidosForm(
        initial={"cliente": pedido.cliente, "productos": pedido.productos.all()}
    )
    return render(
        request, "tienda/pedidosEditar.html", {"form": form, "pedido": pedido}
    )


def pedidos_editar(request, id):
    pedido = get_object_or_404(Pedidos, pk=id)
    if request.method == "POST":
        form = PedidosForm(request.POST)
        if form.is_valid():
            form_cliente = form.cleaned_data["cliente"]
            form_productos = form.cleaned_data["productos"]
            pedido.cliente = form_cliente
            pedido.productos.set(form_productos)
            pedido.save()
            messages.success(request, "Pedido actualizado")
            return redirect("tienda:pedidos_consultar")
    else:
        form = PedidosForm(
            initial={"cliente": pedido.cliente, "productos": pedido.productos.all()}
        )
    return render(
        request, "tienda/pedidosEditar.html", {"form": form, "pedido": pedido}
    )
