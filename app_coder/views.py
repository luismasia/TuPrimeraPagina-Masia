from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_coder.models import Curso
from .forms import AlumnoForm, CursoForm, ProfesorForm
from django.contrib import messages

def inicio(request):
    return render(request, "inicio.html")

def alumnos(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Alumno agregado correctamente.")
            return redirect('alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumnos.html', {'form': form})

def cursos(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Curso agregado correctamente.")
            return redirect('cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos.html', {'form': form})

def profesores(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Profesor agregado correctamente.")
            return redirect('profesores')
    else:
        form = ProfesorForm()
    return render(request, 'profesores.html', {'form': form})

def buscar_curso(request):
    return render(request, "buscar_curso.html")

def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        curso = Curso.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_busqueda.html", {"cursos":curso})
    else:
        return HttpResponse("El curso no existe")