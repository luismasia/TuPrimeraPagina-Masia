from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Alumno, Curso, Profesor, Avatar

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'camada']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'camada': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'camada']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'camada': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'curso', 'camada']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'curso': forms.TextInput(attrs={'class': 'form-control'}),
            'camada': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"
        self.fields['password1'].label = "Contraseña"
        self.fields['password2'].label = "Confirmar contraseña"
        
        for field in self.fields.values():
            field.help_text = None
            field.widget.attrs.update({'class': 'form-control'})

class EditarPerfilForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        labels = {
            'username': 'Nombre de usuario',
            'email': 'Email',
            'password': 'Contraseña',
        }

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']