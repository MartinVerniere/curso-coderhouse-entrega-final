from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import VehicleForm
from .models import Vehicle


# Create your views here.
class VehicleListView(ListView):
    model = Vehicle
    context_object_name = 'vehicles'

    def get_queryset(self):
        super().get_queryset()
        search = self.request.GET.get('search', None)
        if search:
            return Vehicle.objects.filter(Q(marca__icontains=search) | Q(modelo__icontains=search))
        return Vehicle.objects.all()
    
class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('vehicle_list')

    def form_valid(self,form):
        return super().form_valid(form)

class VehicleDetailView(DetailView):
    model = Vehicle

class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    form_class = VehicleForm
    success_url = reverse_lazy('vehicle_list')

    def form_valid(self, form):
        return super().form_valid(form)
    
class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle_list')

@login_required
def delete_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect(reverse_lazy('vehicle_list'))
    return render(request, 'myapp/vehicle_confirm_delete.html', {'vehicle': vehicle})

def home(request):
    return render(request, 'myapp/home.html')

def aboutMe(request):
    return render(request, 'myapp/aboutMe.html')