from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # to the login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # to the logout view
]