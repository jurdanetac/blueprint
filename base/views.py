from django.shortcuts import render

from base.forms import TodoForm
from base.models import Todo

# Create your views here.


def index(request):
    if request.method == "POST":
        todo_form = TodoForm(request.POST)
        new_todo = todo_form.save()
        print(new_todo)
        todos = Todo.objects.all()
        return render(request, "base/partials/todo_list.html", {"todos": todos})

    todos = Todo.objects.all()
    todo_form = TodoForm()

    return render(request, "base/index.html", {"todo_form": todo_form, "todos": todos})
