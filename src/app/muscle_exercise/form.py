from django import forms
from app.muscle_exercise.model import MuscleExercise

class MuscleExerciseForm(forms.ModelForm):
    name = forms.CharField(
        label= 'Nombre del ejercicio del musculo',
        max_length= 100,
        widget= forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre del ejercicio del musculo',
            'maxlength': 100,
        })
    )

    class Meta:
        model = MuscleExercise
        fields = ['name']