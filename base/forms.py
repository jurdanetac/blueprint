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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Loop through all fields and apply a standard styling class
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "p-1 border rounded-md bg-slate-50 text-slate-900 focus:ring-2 focus:ring-blue-400"
                }
            )
