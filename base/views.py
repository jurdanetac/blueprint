from calendar import month
from datetime import date

from http import HTTPStatus

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from base.forms import TodoForm
from base.models import Todo


def generate_month_calendar():
    today = date.today()
    current_year = today.year
    current_month = today.month
    cal = month(theyear=current_year, themonth=current_month)
    return cal


# Create your views here.


@require_GET
def index(request):
    calendar = generate_month_calendar()

    return render(
        request,
        "base/index.html",
        {"calendar": calendar},
    )


@require_GET
def today(request):
    return HttpResponse("")


@require_GET
def backlog(request):
    todos = Todo.objects.all()
    todo_form = TodoForm()

    return render(
        request, "base/partials/backlog.html", {"todos": todos, "todo_form": todo_form}
    )


@require_http_methods(["DELETE"])
def delete_todo(request, todo_id):
    # Safely find the todo item or return a 404 if it doesn't exist
    todo = get_object_or_404(Todo, id=todo_id)

    # Delete the todo from the database
    todo.delete()

    return HttpResponse("", status=HTTPStatus.OK)


@require_POST
def add_todo(request):
    # Create form from the received POST
    todo_form = TodoForm(request.POST)

    # Save it to the database
    todo_form.save()

    # Update todos to re-render the list
    todos = Todo.objects.all()

    return render(request, "base/partials/todo_list.html", {"todos": todos})


@require_GET
def lists(request):
    return HttpResponse("")


@require_GET
def notes(request):
    return HttpResponse("")
