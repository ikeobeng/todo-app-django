from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'date_deadline']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'date_deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

