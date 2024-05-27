from django import forms
from app.progress.model import Progress

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['user', 'exercises', 'weight', 'repetitions']
        widgets = {
            'exercises': forms.CheckboxSelectMultiple()
        }
