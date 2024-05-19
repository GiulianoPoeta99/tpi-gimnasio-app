from django import forms

from app.difficulty_level.models import DifficultyLevel
from app.rutine_type.model import RutineType
from app.user.models import User
from app.rutine.model import Rutine

class RutineForm(forms.ModelForm):
    name = forms.CharField()
    user = forms.ModelChoiceField(queryset=User.objects.all())
    difficulty_level = forms.ModelChoiceField(queryset=DifficultyLevel.objects.all())
    rutine_type = forms.ModelMultipleChoiceField(queryset=RutineType.objects.all())

    class Meta:
        model = Rutine
        fields = ['name', 'user', 'difficulty_level', 'rutine_type']
