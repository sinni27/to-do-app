from django import forms
from to_do_list.models import Task

class AddNewForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
