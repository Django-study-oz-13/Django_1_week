<<<<<<< HEAD:todoproject/todo/urls.py
from django.urls import path

from todo import views

urlspatterns = [
    path('', views.todo_list, name='todo_list'),
]
=======
from django.contrib import admin
from django.urls import path, include

utlpatterns = [
    path('admin/', admin.site.urls),
    ]
>>>>>>> 49a686e (💡 Todo 모델 생성):todo/urls.py
