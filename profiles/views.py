from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView
from .forms import CreateProfileForm, EditProfileForm, AvatarForm
from .models import Avatar

# Create your views here.

class UserView(DetailView, LoginRequiredMixin):
    model = User
    template_name = "profiles/profile.html"
    context_object_name = "user"

    def get_object(self):
        return self.request.user

class UserRegisterView(CreateView):
    model = User
    form_class = CreateProfileForm
    template_name = "profiles/profile_create.html"
    success_url = reverse_lazy('profile_login')

class UserUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    form_class = EditProfileForm
    template_name = "profiles/profile_update.html"
    success_url = reverse_lazy('profile')

    context_object_name = "user"

    def get_object(self):
        return self.request.user

class UserLoginView(LoginView):
    template_name = "profiles/profile_login.html"

    def get_success_url(self):
        return reverse_lazy('profile')

class UserLogoutView(LogoutView):
    template_name = "profiles/profile_logout.html"
    next_page = reverse_lazy('profile_login')

@login_required # Asegura que el usuario esté autenticado para editar su perfil
def profile_update(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        try:
            avatar = request.user.avatar
        except Avatar.DoesNotExist:
            avatar = None
            
        if avatar:
            avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        else:
            avatar_form = AvatarForm(request.POST, request.FILES)


        if form.is_valid() and avatar_form.is_valid():
            form.save()
            avatar_instance = avatar_form.save(commit=False)
            avatar_instance.user = request.user
            avatar_instance.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
        if hasattr(request.user, 'avatar'):
            avatar_form = AvatarForm(instance=request.user.avatar)
        else:
            avatar_form = AvatarForm()
    return render(request, 'profiles/profile_update.html', {'form': form, 'avatar_form': avatar_form})