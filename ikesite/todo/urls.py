from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

app_name = 'todo'

urlpatterns = [
    path('open/', views.OpenView.as_view(), name='open'),  # open view
    path('', views.MainView.as_view(), name='todo_list'),  # list of all todos
    path('delete/<int:pk>/', views.DeleteTodoView.as_view(), name='delete'),  # delete Todo URL pattern
    path('update/<int:pk>/', views.UpdateTodoView.as_view(), name='update'),  # update Todo URL pattern
    path('login/', LoginView.as_view(), name='login'),  # login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # logout view
]

