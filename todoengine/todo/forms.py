from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']

        attrs = {
            'class': 'form-control',
            'placeholder': 'Enter todo e.g. Play with cat',
        }

        widgets = {
            'title': forms.TextInput(attrs=attrs)
        }



