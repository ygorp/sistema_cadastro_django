from django.urls import path
from app_cadastro_usuarios import views

urlpatterns = [
    path('', views.home, name='home'),
]
