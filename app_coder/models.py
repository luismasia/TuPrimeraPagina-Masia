from django.db import models

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
    