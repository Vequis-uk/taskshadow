from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout

#Model imports
from .models import TaskShadowTodo

@login_required
def todo_list(request):
    todos = TaskShadowTodo.objects.filter(user=request.user)
    return render(request, 'todo_list.html', {'todos': todos})

#Add To-do List View
@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        TaskShadowTodo.objects.create(user=request.user, title=title)
    return redirect('todo_list')

#Mark Complete To-do List View
@login_required
def mark_complete(request, todo_id):
    todo = TaskShadowTodo.objects.get(pk=todo_id)
    todo.completed =not todo.completed
    todo.save()
    return redirect('todo_list')
