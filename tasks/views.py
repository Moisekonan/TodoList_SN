from django.http import Http404
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

@login_required()
def index(request):
    # TODO: use pagination
    tasks_list = Task.objects.filter(user=request.user)
    paginator = Paginator(tasks_list, 2)
    
    page_number = request.GET.get('page')
    tasks = paginator.get_page(page_number)
    return render(request, 'tasks/index.html', {'tasks': tasks})

# TODO: add login_required
@login_required()
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

# TODO: add login_required
@login_required()
def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    # TODO: check whether the logged-in user is the author of the task
    if task.user != request.user:
        raise Http404("Vous n'êtes pas autorisé à modifier cette tâche.")
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

# TODO: add login_required
@login_required()
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    # TODO: check whether the logged-in user is the author of the task
    if task.user != request.user:
        raise Http404("Vous n'êtes pas autorisé à supprimer cette tâche.")
    
    task.delete()
    return redirect('index')
