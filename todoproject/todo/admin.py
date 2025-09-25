from django.contrib import admin
<<<<<<< Updated upstream:todoproject/todo/admin.py
from .models import Todo

# Register your models here.
admin.site.register(Todo)
=======
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]
>>>>>>> Stashed changes:todo/admin.py
