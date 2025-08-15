from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar

class CreateProfileForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
            'username': 'Nombre de Usuario',
        }    

class EditProfileForm(UserChangeForm):
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Email',
            'username': 'Nombre de Usuario',
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']