from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from .forms import TodoForm
from .models import Todo


class TodoList(View):
    def get(self, request):
        form = TodoForm()
        tasks = Todo.objects.all()
        return render(request, 'todo/index.html', context={'form': form, 'tasks': tasks})

    def post(self, request):
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect('todo_list_url')


def todo_completed(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('todo_list_url')


def delete_completed(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('todo_list_url')


def delete_all(request):
    Todo.objects.all().delete()
    return redirect('todo_list_url')
