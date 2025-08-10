from django.contrib import admin
from .models import Vehicle

# Register your models here.
register_models = [Vehicle]

admin.site.register(register_models)