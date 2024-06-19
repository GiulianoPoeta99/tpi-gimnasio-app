# forms.py
from django import forms
from app.user.model import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-xl',
            'placeholder': 'Password'
        })
    )
    
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-xl',
            'placeholder': 'Confirm Password'
        })
    )
    
    gender = forms.ChoiceField(
        choices=[(True, 'Male'), (False, 'Female')],
        widget=forms.Select(attrs={
            'class': 'form-control form-control-xl'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password', 'gender']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control form-control-xl',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control form-control-xl',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-xl',
                'placeholder': 'Email'
            }),
        }
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está en uso.")
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Las contraseñas no coinciden.")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_male = self.cleaned_data["gender"]
        if commit:
            user.save()
        return user

class UserForm(forms.ModelForm):
    password = forms.CharField(
        label='Contraseña',
        required=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
    )
    
    first_name = forms.CharField(
        label='Nombre',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre'
        })
    )
    
    last_name = forms.CharField(
        label='Apellido',
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apellido'
        })
    )
    
    email = forms.EmailField(
        label='Correo Electrónico',
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo Electrónico'
        })
    )
    
    gender = forms.ChoiceField(
        choices=[(True, 'Male'), (False, 'Female')],
        widget=forms.Select(attrs={
            'class': 'form-control form-control-xl'
        })
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password', 'is_male']

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["password"]:
            user.set_password(self.cleaned_data["password"])
        user.is_male = self.cleaned_data["gender"]
        if commit:
            user.save()
        return user
