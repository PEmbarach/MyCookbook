from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout')
]
