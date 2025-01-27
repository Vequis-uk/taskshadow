from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm

# Model imports
from .models import TaskShadowTodo


@login_required
def todo_list(request):
    todos = TaskShadowTodo.objects.filter(user=request.user).order_by(
        '-priority', 'title')
    return render(request, 'todo_list.html', {'todos': todos})


# Add To-do List View
@login_required
def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        priority = request.POST.get('priority', TaskShadowTodo.MEDIUM)
        TaskShadowTodo.objects.create(
            user=request.user, title=title, priority=priority)
        messages.success(request, "Todo added successfully!")
    else:
        messages.error(request, "Failed to add Todo. Please try again.")
    return redirect('todo_list')


# Update To-do Priority
@login_required
def update_priority(request, todo_id):
    todo = get_object_or_404(TaskShadowTodo, id=todo_id, user=request.user)
    if request.method == 'POST':
        new_priority = request.POST.get('priority', TaskShadowTodo.MEDIUM)
        todo.priority = new_priority
        todo.save()
        messages.success(
            request, f"Priority for '{todo.title}' updated successfully!")
        return redirect('todo_list')
    return render(request, 'update_priority.html', {'todo': todo})


# Mark Complete To-do List View
@login_required
def mark_complete(request, todo_id):
    todo = get_object_or_404(TaskShadowTodo, id=todo_id, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    status = "completed" if todo.completed else "marked as incomplete"
    messages.success(request, f"Todo '{todo.title}' {status} successfully!")
    return redirect('todo_list')


# Delete To-do List View
@login_required
def delete_todo(request, todo_id):
    todo = get_object_or_404(TaskShadowTodo, id=todo_id, user=request.user)
    todo.delete()
    messages.success(request, f"Todo '{todo.title}' deleted successfully!")
    return redirect('todo_list')


# Register View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome!")
            return redirect('todo_list')
        else:
            messages.error(
                request,
                "Registration failed. Please check the form and try again.")
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


# Login View
def user_login(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful! Welcome back!")
            return redirect('todo_list')
        else:
            messages.error(
                request,
                "Login failed. Please check your username and password.")
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'login.html', {'form': form})


# Logout View
@login_required
def user_logout(request):
    django_logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('login')
