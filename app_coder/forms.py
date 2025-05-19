from django import forms
from .models import Alumno, Curso, Profesor

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