from django import forms
from django.forms import ModelForm
from . import models

class ForumusersForm(ModelForm):
    class Meta:
        model = models.Forumusers
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput
        }
        
class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
class EditProfileForm(ModelForm):
    password = forms.CharField(
        label="Nueva Contraseña (opcional)",
        widget=forms.PasswordInput,
        required=False
    )
    confirm_password = forms.CharField(
        label="Confirmar Nueva Contraseña",
        widget=forms.PasswordInput,
        required=False
    )

    class Meta:
        model = models.Forumusers
        fields = ['username', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['email'].required = False

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password or confirm_password:
            if password != confirm_password:
                self.add_error('confirm_password', 'Las contraseñas no coinciden')
        return cleaned_data