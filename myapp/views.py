from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import VehicleForm
from .models import Vehicle
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class VehicleListView(ListView):
    model = Vehicle
    context_object_name = 'vehicles'

    def get_queryset(self):
        super().get_queryset()
        search = self.request.GET.get('search', None)
        if search:
            return Vehicle.objects.filter(modelo__icontains=search)
        return Vehicle.objects.all()
    
class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('vehicle_list')

    def form_valid(self,form):
        return super().form_valid(form)

class VehicleDetailView(DetailView):
    model = Vehicle

class VehicleUpdateView(UpdateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('vehicle_list')

    def form_valid(self, form):
        return super().form_valid(form)
    
class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')

def home(request):
    return render(request, 'myapp/home.html')

def aboutMe(request):
    return render(request, 'myapp/aboutMe.html')