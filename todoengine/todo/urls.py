from django.urls import path
from .views import TodoList, delete_all, todo_completed, delete_completed

urlpatterns = [
    path('', TodoList.as_view(), name='todo_list_url'),
    path('complete/<str:todo_id>', todo_completed, name='todo_completed_url'),
    path('delete-all/', delete_all, name='delete_all_url'),
    path('delete-completed/', delete_completed, name='delete_completed_url'),
]