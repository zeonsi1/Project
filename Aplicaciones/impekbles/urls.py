from django.contrib import admin
from django.urls import path
from . import views
from .views import email_view
urlpatterns = [
    path('base', views.index, name='index'),
    path('', views.home, name='home'),
    path('create-account', views.createuser, name='create-account'),
    path('login', views.login, name='login'),
    path('productos', views.producto, name='producto'),
    path('contacto', views.contacto, name='contacto'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('signup/', views.signup, name='signup'),
    path('enviar-correo/', email_view, name='enviar_correo'),
]
