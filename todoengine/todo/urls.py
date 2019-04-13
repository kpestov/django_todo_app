from django.urls import path
from .views import show_todo_list

urlpatterns = [
    path('', show_todo_list, name='todo_list_url'),
]