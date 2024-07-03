from django import forms
from .models import Info,Portfolio,Project

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'

class PortfolioForm(forms.ModelForm):
    class Meta:
        model=Portfolio
        fields='__all__'


from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields = ['Project_Name','image', 'Description', 'Link']

# forms.py

from django import forms
from .models import UserID

class UserIDForm(forms.ModelForm):
    class Meta:
        model = UserID
        fields = ['identifier']
