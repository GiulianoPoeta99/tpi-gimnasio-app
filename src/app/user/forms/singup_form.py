from django import forms
from app.user.model import User
    
class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El correo electrónico ya está en uso.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user