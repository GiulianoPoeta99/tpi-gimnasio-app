from django import forms
from app.assign_rutine.model import AssignRutine
from app.user.model import User
from app.trainer.model import Trainer
from app.rutine.model import Rutine

class AssignRutineForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Usuario',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    trainer = forms.ModelChoiceField(
        queryset=Trainer.objects.all(),
        label='Entrenador',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    rutine = forms.ModelChoiceField(
        queryset=Rutine.objects.all(),
        label='Rutina',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = AssignRutine
        fields = ['user', 'trainer', 'rutine']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     # Aquí puedes agregar validaciones adicionales si las necesitas
    #     return cleaned_data
