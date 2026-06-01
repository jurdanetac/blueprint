from calendar import month
from datetime import date

from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# from django.views.decorators.csrf import csrf_exempt

from base.forms import TodoForm
from base.models import Todo

# Create your views here.


def delete_todo(request, todo_id):
    if request.method != "POST":
        return HttpResponse(status=HTTPStatus.METHOD_NOT_ALLOWED)

    # Safely find the todo item or return a 404 if it doesn't exist
    todo = get_object_or_404(Todo, id=todo_id)

    # Delete the todo from the database
    todo.delete()

    return HttpResponse("", status=HTTPStatus.OK)


def generate_month_calendar():
    today = date.today()
    current_year = today.year
    current_month = today.month
    cal = month(theyear=current_year, themonth=current_month)
    return cal


def index(request):
    if request.method == "POST":
        todo_form = TodoForm(request.POST)
        new_todo = todo_form.save()
        todos = Todo.objects.all()
        return render(request, "base/partials/todo_list.html", {"todos": todos})

    todos = Todo.objects.all()
    todo_form = TodoForm()

    calendar = generate_month_calendar()

    return render(
        request,
        "base/index.html",
        {"todo_form": todo_form, "todos": todos, "calendar": calendar},
    )
