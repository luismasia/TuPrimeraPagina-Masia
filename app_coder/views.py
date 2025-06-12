from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_coder.models import Curso, Avatar, Post
from .forms import AlumnoForm, CursoForm, ProfesorForm, RegistroUsuarioForm, EditarPerfilForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

def inicio(request):
    return render(request, "inicio.html")

@login_required
def foro(request):
    return render(request, "foro.html")

@login_required
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

@login_required
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

@login_required
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

@login_required
def buscar(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        curso = Curso.objects.filter(nombre__icontains = nombre)
        return render(request, "resultado_busqueda.html", {"cursos":curso})
    else:
        return HttpResponse("El curso no existe")

def about(request):
    return render(request, "about.html")

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('inicio')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def editar_perfil(request):
    try:
        avatar_instance = request.user.avatar
    except Avatar.DoesNotExist:
        avatar_instance = Avatar(user=request.user)

    if request.method == 'POST':
        perfil_form = EditarPerfilForm(request.POST, instance=request.user)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar_instance)

        if perfil_form.is_valid() and avatar_form.is_valid():
            perfil_form.save()
            avatar_form.save()
            return redirect('inicio')

    else:
        perfil_form = EditarPerfilForm(instance=request.user)
        avatar_form = AvatarForm(instance=avatar_instance)

    return render(request, 'editar_perfil.html', {
        'perfil_form': perfil_form,
        'avatar_form': avatar_form,
        'avatar_instance': avatar_instance,        
    })

class ForoListView(ListView):
    model = Post
    template_name = 'pages.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('pages')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_form.html'
    fields = ['titulo', 'contenido']
    success_url = reverse_lazy('pages')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('pages')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor