from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def home(request):
    return render(request, 'home.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks_list')
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form': form})
