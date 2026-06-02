from django import forms

from base.models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["task", "due_on"]
        widgets = {
            # This overrides the default widget for 'due_on' with the custom HTML5 date picker widget
            "due_on": forms.DateInput(attrs={"type": "date"}),
        }
