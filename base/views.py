from calendar import month
from datetime import date

from http import HTTPStatus

from django.http import HttpResponse, JsonResponse
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


@require_GET
def get_minical_json(request):
    cal = generate_month_calendar()
    splitted_cal = cal.split()

    month = splitted_cal[0]
    year = int(splitted_cal[1])
    weekdays = splitted_cal[2:9]
    days = splitted_cal[9:]
    days = [int(day) for day in days]

    weeks = [
        days[0:7],
        days[7:14],
        days[14:21],
        days[21:28],
    ]

    # check if not february
    if len(days) > 28:
        weeks.append(days[28:])

    context = {
        "year": year,
        "month": month,
        "weeks": weeks,
    }

    return render(request, "base/partials/minical.html", context)

    return JsonResponse(
        {
            "year": year,
            "month": month,
            "weeks": weeks,
        }
    )


### ROUTES


@require_GET
def index(request):
    context = {
        "calendar": generate_month_calendar(),
        "overdue_todos": Todo.objects.overdue(),
        "today_pending_todos": Todo.objects.today_pending(),
        "today_completed_todos": Todo.objects.today_completed(),
    }

    return render(request, "base/index.html", context)


@require_GET
def today(request):
    context = {
        "overdue_todos": Todo.objects.overdue(),
        "today_pending_todos": Todo.objects.today_pending(),
        "today_completed_todos": Todo.objects.today_completed(),
    }

    return render(request, "base/partials/today.html", context)


@require_GET
def backlog(request):
    context = {
        "pending_todos": Todo.objects.pending(),
        "todo_form": TodoForm(),
    }

    return render(request, "base/partials/backlog.html", context)


@require_GET
def completed(request):
    context = {"completed": Todo.objects.completed()}

    return render(request, "base/partials/completed.html", context)


@require_GET
def scheduled(request):
    context = {"scheduled": Todo.objects.scheduled()}

    return render(request, "base/partials/scheduled.html", context)


@require_GET
def lists(request):
    return HttpResponse("")


@require_GET
def notes(request):
    return HttpResponse("")


@require_POST
def add_todo(request):
    # Create form from the received POST
    todo_form = TodoForm(request.POST)

    # Save it to the database
    todo_form.save()

    context = {
        # Update todos to re-render the backlog
        "pending": Todo.objects.pending()
    }

    return render(request, "base/partials/todo_list.html", context)


@require_http_methods(["DELETE"])
def delete_todo(request, todo_id):
    # Safely find the todo item or return a 404 if it doesn't exist
    todo = get_object_or_404(Todo, id=todo_id)

    # Delete the todo from the database
    todo.delete()

    return HttpResponse("", status=HTTPStatus.OK)


@require_http_methods(["PATCH"])
def check_todo(request, todo_id):
    # Safely find the todo item or return a 404 if it doesn't exist
    todo = get_object_or_404(Todo, id=todo_id)

    todo.completed = True
    todo.save()

    return HttpResponse("", status=HTTPStatus.OK)
