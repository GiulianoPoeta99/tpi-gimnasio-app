from django import forms
from app.difficulty_level.models import DifficultyLevel
from app.rutine_type.model import RutineType
from app.user.models import User
from app.rutine.model import Rutine

class RutineForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre de la Rutina',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre de la rutina',
            'maxlength': 60,
        })
    )
    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label='Usuario',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    difficulty_level = forms.ModelChoiceField(
        queryset=DifficultyLevel.objects.all(),
        label='Nivel de Dificultad',
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    rutine_type = forms.ModelMultipleChoiceField(
        queryset=RutineType.objects.all(),
        label='Tipos de Rutina',
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Rutine
        fields = ['name', 'user', 'difficulty_level', 'rutine_type']

    def clean(self):
        cleaned_data = super().clean()
        difficulty_level = cleaned_data.get('difficulty_level')
        if difficulty_level is None:
            raise forms.ValidationError('Debe especificar un nivel de dificultad para la rutina.')
        return cleaned_data
