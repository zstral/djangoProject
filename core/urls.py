from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forum/', views.forum, name='forum'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('<str:section>/', views.home, name='section'),
]
