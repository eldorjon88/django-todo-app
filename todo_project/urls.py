from django.contrib import admin
from django.urls import path, include
from tasks import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_views.home, name='home'),
    path('tasks/', include([
        path('', task_views.task_list, name='tasks_list'),
        path('create/', task_views.task_create, name='task_create'),
    ])),
]
