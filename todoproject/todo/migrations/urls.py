from django.urls import path
from . import views

urlspatterns = [
    path('', views.todo_list, name='todo_list'),
]