from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)  

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=True, null=True)  
    descripcion = models.TextField(blank=True, null=True)  # Campo de descripción
    stock = models.PositiveIntegerField(default=0)  # Campo de stock (números positivos)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)  # Campo de imagen

    def __str__(self):
        return self.nombre
    
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=255)
    celular = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=255)

class Meta:
    db_table = 'usuarios'


