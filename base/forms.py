from django.forms import ModelForm

from base.models import Todo


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ["task"]
