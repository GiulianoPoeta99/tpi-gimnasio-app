from django import forms
from app.user.model import User  
from app.trainer.model import Trainer 

class TrainerForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Usuario',
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select form-control-lg',
            'id': 'user'
        })
    )

    is_verify = forms.BooleanField(
        label='Verificado',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'is_verify'
        })
    )

    RATE_CHOICES = [(i, i) for i in range(1, 6)]  

    rate = forms.ChoiceField(
        label='Calificación',
        choices=RATE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-select form-control-lg',
            'id': 'rate'
        })
    )

    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        label='Usuarios',
        required=False,
        widget=forms.CheckboxSelectMultiple
    )


    class Meta:
        model = Trainer
        fields = ['user', 'is_verify', 'rate', 'users']

