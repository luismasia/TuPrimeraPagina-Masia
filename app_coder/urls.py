from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio),
    path("profesores" , views.profesores , name="profesores"),
    path("cursos" , views.cursos , name="cursos"),
    path("alumnos" , views.alumnos , name="alumnos" ),
    path("contacto" , views.contacto),
    #path("alta_curso/<nombre>" , views.alta_curso)
    path("alta_curso", views.curso_formulario),
    path("buscar_curso",views.buscar_curso),
    path("buscar",views.buscar)

]
