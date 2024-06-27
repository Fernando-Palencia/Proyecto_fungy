from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from usuarios.models import  Producto, Usuario

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio','categoria', 'descripcion', 'stock', 'imagen']    


class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo', widget=forms.EmailInput(attrs={
        'class': 'form-group',
        'placeholder': 'Introduzca su correo'
    }))
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={
        'class': 'form-group',
        'placeholder': 'Introduzca su contraseña'
    }))

class UsuarioForm(forms.ModelForm):
    confirm_password = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput(attrs={
        'class': 'form-group',
        'placeholder': 'Confirme su contraseña'
    }))

    class Meta:
        model = Usuario
        fields = ['nombre', 'correo', 'direccion', 'celular', 'contrasena']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'Introduzca su nombre'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-group',
                'placeholder': 'Introduzca su correo'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'Introduzca su dirección'
            }),
            'celular': forms.TextInput(attrs={
                'class': 'form-group',
                'placeholder': 'Introduzca su celular'
            }),
            'contrasena': forms.PasswordInput(attrs={
                'class': 'form-group',
                'placeholder': 'Introduzca su contraseña'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        contrasena = cleaned_data.get("contrasena")
        confirm_password = cleaned_data.get("confirm_password")

        if contrasena != confirm_password:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.contrasena = make_password(self.cleaned_data["contrasena"])  # Cifra la contraseña
        if commit:
            user.save()
        return user
