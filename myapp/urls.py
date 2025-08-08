from django.urls import path
from . import views

urlpatterns = [
    path('', views.a, name='a'),
    path('b', views.b, name='b'),
    path('c', views.c, name='c'),
]