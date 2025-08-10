from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['marca', 'modelo', 'descripcion', 'fecha_creacion']
        labels = {
            'marca': 'Marca del vehiculo',
            'modelo': 'Modelo del vehiculo',
            'descripcion': 'Descripcion del vehiculo',
            #'image': 'Foto del vehiculo',
            'fecha_creacion': 'Fecha de construccion del vehiculo'
        }