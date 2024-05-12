from django.shortcuts import render, redirect
from tienda.models import Producto, Cliente
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
    producto = Producto(nombre=nombre, precio=precio, descripcion=descripcion)
    producto.save()
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


'''
CLIENTE CLIENTE CLIENTE CLIENTE CLIENTE CLIENTE 
'''
def cliente_consultar(request):
        #buscador y mostrar toda la base de datos
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        print(busqueda)
        clientes = Cliente.objects.filter(nombre__icontains = busqueda)
    else:
        clientes = Cliente.objects.all()
    return render(request,"tienda/cliente.html", {"clientes":clientes})

def cliente_create(request): #guardar
    # if request.method == "POST":
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        telefono = request.POST["telefono"]
        cliente = Cliente(nombre=nombre, email=email, telefono=telefono)
        cliente.save()
        messages.success(request, "Cliente agregado")
        # Redirigir a la vista de lista clientes
        return redirect("tienda:cliente_consultar")
    # else:
    #     form = ClienteForm()
    # return render(request, 'tienda/cliente_edit.html', {'form': form})

def cliente_eliminar(request, id):
    cliente = Cliente.objects.filter(pk=id)
    cliente.delete()
    messages.success(request, "Cliente eliminado")
    return redirect("tienda:cliente_consultar")



# mostrar en detalles y modificar un cliente
def cliente_detalle(request, id):
    cliente = Cliente.objects.get(pk=id)
    return render(request, "tienda/clienteEditar.html", {"cliente": cliente})

def cliente_editar(request, id):
    nombre = request.POST["nombre"]
    email = request.POST["email"]
    telefono = request.POST["telefono"]
    # campo oculto en el formulario editar
    id = request.POST['id']
    Cliente.objects.filter(pk=id).update(
        nombre=nombre, email=email, telefono=telefono
    )
    messages.success(request, "Cliente actualizado")
    return redirect("tienda:cliente_consultar")