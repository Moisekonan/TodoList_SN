from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required()
def index(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/index.html', {'tasks': tasks})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})


def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('index')
