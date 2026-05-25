from django.urls import path

from . import views

urlpatterns = [
    # GET: Renders homepage
    path("", views.index, name="index"),
    # POST: Deletes a todo item
    path("<int:todo_id>/delete/", views.delete_todo, name="delete-todo"),
]
