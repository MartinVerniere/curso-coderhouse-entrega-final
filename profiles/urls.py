from django.urls import path
from . import views

# SE CAMBIARON EL NOMBRE DE LOS ARCHIVO HTML PARA QUE FUNCIONEN CON LAS VISTAS
# VIEWS usa _form para create and update views, y nombreModeloMinuscula_[detail/list/confirm_delete] para las otras vistas

urlpatterns = [
    path('', views.UserView.as_view(), name='profile'),
    path('create', views.UserRegisterView.as_view(), name='profile_create'),
    path('edit', views.profile_update, name='profile_update'),
    path('login', views.UserLoginView.as_view(), name='profile_login'),
    path('logout', views.UserLogoutView.as_view(), name='profile_logout'),
]