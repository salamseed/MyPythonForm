from django import forms
from .models import DailyTask
class updateform(forms.ModelForm):
    class Meta:
        model = DailyTask
        fields = ['task','priority','date']