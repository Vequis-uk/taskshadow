from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('todo/<int:todo_id>/delete/', views.delete_todo, name='delete_todo'),
    path(
        'todo/<int:todo_id>/complete/', views.mark_complete,
        name='complete_todo'),
    path('add/', views.add_todo, name='add_todo'),
    path(
        'update-priority/<int:todo_id>/',
        views.update_priority, name='update_priority'),
    path('update-title/<int:todo_id>/', views.update_todo_title, name='update_todo_title'),

]
