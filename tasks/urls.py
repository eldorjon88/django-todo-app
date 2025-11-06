from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='tasks_list'),
    path('create/', views.task_create, name='task_create'),
]
