from django import forms
from app.trainer.model import Trainer

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['user', 'is_verify', 'rate']
        widgets = {
            'is_verify': forms.CheckboxInput(),
            'rate': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
