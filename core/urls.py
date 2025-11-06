from django.contrib import admin
from django.urls import path, include
from tasks import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_views.home, name='home'),  # Home page
    path('tasks/', include('tasks.urls')),   # tasks app URLlarini qo‘shish
]
