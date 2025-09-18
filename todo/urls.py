from django.contrib import admin
from django.urls import path, include

utlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', views.todo_post, name='todo_post'),
    ]