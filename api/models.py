from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarea(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200)
    completada = models.BooleanField(default=False, blank=True, null=True)
    descripcion = models.TextField(null=True, blank=True)
    fecha = models.DateTimeField(null=True)
    
    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['fecha']

    def __str__(self):
        return self.nombre
