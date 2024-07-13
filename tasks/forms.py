from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'time_limit']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        time_limit = cleaned_data.get("time_limit")

        if not title:
            self.add_error('title', 'This field is required.')
        if not description:
            self.add_error('description', 'This field is required.')
        if not time_limit:
            self.add_error('time_limit', 'This field is required.')