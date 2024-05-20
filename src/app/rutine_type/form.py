from django import forms
from app.rutine_type.model import RutineType

class RutineTypeForm(forms.ModelForm):
    name = forms.CharField(
        label='Nombre del tipo de rutina',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el nombre del tipo de rutina',
            'maxlength': 100,
        })
    )

    class Meta:
        model = RutineType
        fields = ['name']
