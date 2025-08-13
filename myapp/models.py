from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Vehicle(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to='vehicles/images/', null=True, blank=True)

    def __str__(self):
        return f"Este es un auto de marca {self.marca} - modelo {self.modelo}"