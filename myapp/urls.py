from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vehicles', views.VehicleListView.as_view(), name='vehicle_list'),
    path('vehicles/<int:pk>', views.VehicleDetailView.as_view(), name='vehicle_details'),
    path('vehicles/create', views.VehicleCreateView.as_view(), name='vehicle_create'),
    path('vehicles/update/<int:pk>', views.VehicleUpdateView.as_view(), name='vehicle_update'),
    #path('vehicles/delete/<int:pk>', views.VehicleDeleteView.as_view(), name='vehicle_delete'),
    path('vehicles/delete/<int:pk>', views.delete_vehicle, name='vehicle_delete'),
    path('aboutme', views.aboutMe, name='about_me'),
]