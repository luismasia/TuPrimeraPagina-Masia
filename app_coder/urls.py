from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .views import (
    ForoListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    path("", views.inicio, name="inicio"),   
    path("profesores", views.profesores, name="profesores"),
    path("cursos", views.cursos, name="cursos"),
    path("alumnos", views.alumnos, name="alumnos" ),
    path("buscar_curso", views.buscar_curso, name="buscar_curso"),
    path("buscar", views.buscar),
    path("about", views.about, name="about"),
    path("signup", views.registrar_usuario, name="signup"),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('editar_perfil', views.editar_perfil, name='editar_perfil'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='password_change.html',
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'
    ), name='password_change_done'),
    path("pages", ForoListView.as_view(), name="pages"),
    path("pages/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("pages/nuevo/", PostCreateView.as_view(), name="post_create"),
    path("pages/<int:pk>/editar/", PostUpdateView.as_view(), name="post_edit"),
    path("pages/<int:pk>/borrar/", PostDeleteView.as_view(), name="post_delete"),
]