from django.urls import path

from . import views

urlpatterns = [
    # GET: Renders homepage
    path("", views.index, name="index"),
    # GET: Renders active section
    path("partials/today/", views.today, name="today"),
    path("partials/backlog/", views.backlog, name="backlog"),
    path("partials/scheduled/", views.scheduled, name="scheduled"),
    path("partials/completed/", views.completed, name="completed"),
    path("partials/lists/", views.lists, name="lists"),
    path("partials/notes/", views.notes, name="notes"),
    # POST: Creates a todo item
    path("todos/add/", views.add_todo, name="add-todo"),
    # DELETE: Deletes a todo item
    path("todos/<int:todo_id>/delete/", views.delete_todo, name="delete-todo"),
    # PATCH: Marks a todo item as completed
    path("todos/<int:todo_id>/check/", views.check_todo, name="check-todo"),
    # PUT: Updates a todo item
    # path("todos/<int:todo_id>/edit/", views.edit_todo, name="edit-todo"),
]
