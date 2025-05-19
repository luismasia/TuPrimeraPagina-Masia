from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("profesores", views.profesores, name="profesores"),
    path("cursos", views.cursos, name="cursos"),
    path("alumnos", views.alumnos, name="alumnos" ),
    path("buscar_curso", views.buscar_curso, name="buscar_curso"),
    path("buscar", views.buscar)
]