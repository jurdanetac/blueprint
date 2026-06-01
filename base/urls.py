from django.urls import path

from . import views

urlpatterns = [
    # GET: Renders homepage
    path("", views.index, name="index"),
    # POST: Creates a todo item
    path("todos/add/", views.add_todo, name="add-todo"),
    # DELETE: Deletes a todo item
    path("todos/<int:todo_id>/delete/", views.delete_todo, name="delete-todo"),
    # PUT: Updates a todo item
    # path("todos/<int:todo_id>/edit/", views.edit_todo, name="edit-todo"),
]
