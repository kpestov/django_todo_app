from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

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


def send_list(request):
    tasks = Todo.objects.filter(complete=False)

    subject = 'Todo list'
    message = '\n'.join(['-' + i.title for i in tasks])
    from_email = 'kpestov91@gmail.com'
    recepients = ['kpestov91@gmail.com']

    try:
        send_mail(
            subject,
            message,
            from_email,
            recepients,
        )

    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    return redirect('todo_list_url')



