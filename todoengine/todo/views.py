from django.shortcuts import render


def show_todo_list(request):
    return render(request, 'todo/index.html')