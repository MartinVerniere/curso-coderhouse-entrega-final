from django.db import models

# Create your models here.

class Vehicle(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    fecha_creacion = models.DateField()
    descripcion = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='vehicles/images/', null=True, blank=True)

    def __str__(self):
        return f"Este es un auto de marca {self.marca} - modelo {self.modelo}"