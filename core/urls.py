from django.urls import path
from . import views
from .views import forum

urlpatterns = [
    path('', views.home, name='home'),
    path('foro/', views.forum, name='forum'),
    path('registrarse/', views.signup, name='signup'),
    path('iniciar-sesion/', views.login, name='login'),
    path('micuenta/', views.account, name='account'),
]
