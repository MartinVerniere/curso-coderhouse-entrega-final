from django import forms
from .models import Vehicle
from ckeditor.widgets import CKEditorWidget

class VehicleForm(forms.ModelForm):
    descripcion = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Vehicle
        fields = ['marca', 'modelo', 'descripcion','imagen', 'fecha_creacion']
        labels = {
            'marca': 'Marca del vehiculo',
            'modelo': 'Modelo del vehiculo',
            'descripcion': 'Descripcion del vehiculo',
            'imagen': 'Foto del vehiculo',
            'fecha_creacion': 'Fecha de construccion del vehiculo'
        }