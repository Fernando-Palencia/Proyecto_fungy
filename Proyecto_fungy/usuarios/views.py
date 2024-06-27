# views.py
from pyexpat.errors import messages
from django.shortcuts import render, redirect
from usuarios.models import Producto, Usuario
from .forms import LoginForm, ProductoForm, UsuarioForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Usuario

from django.contrib.auth import logout


def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UsuarioForm()
    return render(request, 'register.html', {'form': form})

def authenticate_user(email, password):
    try:
        user = Usuario.objects.get(correo=email)
        if check_password(password, user.contrasena):
            return user
        else:
            return None
    except Usuario.DoesNotExist:
        return None

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate_user(email, password)
            if user:
                messages.success(request, 'Inicio de sesión exitoso')
                return redirect('secret')
            else:
                messages.error(request, 'Correo o contraseña incorrectos')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')  # Redirige a la lista de productos
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    return redirect('listar_productos')

def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

def dashboard(request):
    return render(request, 'dashboard.html')

def index_view(request):
    return render(request, 'index.html')

def productos_view(request):
    return render(request, 'productos.html')

def paso_paso_view(request):
    return render(request, 'paso_paso.html')

def capacitaciones_view(request):
    return render(request, 'capacitaciones.html')

def conocenos_view(request):
    return render(request, 'conocenos.html')

def blog_view(request):
    return render(request, 'blog.html')

def secret_view(request):
    return render(request, 'secret.html')

def mas_view(request):
    return render(request, 'que_mas.html')
