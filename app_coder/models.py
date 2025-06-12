from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha_creacion']

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    camada = models.IntegerField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    camada = models.IntegerField()

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.imagen}"
    