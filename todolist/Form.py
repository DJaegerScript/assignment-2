from django import forms


class TodoListForm(forms.Form):
    title = forms.CharField(required=True, label="Title")
    description = forms.CharField(required=True, label="Description")