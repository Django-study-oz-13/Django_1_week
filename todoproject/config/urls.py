"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD:todoproject/config/urls.py
    path('todo/', include('todo.urls')),
=======

    path('<int:pk>/', views.todo_detail, name='todo_detail'),

    path('post/', views.todo_post, name='todo_post'),

    path('<int:pk>/edit/', views.todo_edit, name='todo_edit'),
>>>>>>> 01f535b (내 변경사항 저장):config/urls.py
]
