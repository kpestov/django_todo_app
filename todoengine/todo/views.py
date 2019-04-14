from django.shortcuts import render

from .forms import TodoForm
from .models import Todo


def show_todo_list(request):
    form = TodoForm()
    tasks = Todo.objects.all()
    return render(request, 'todo/index.html', context={'form': form, 'tasks': tasks})