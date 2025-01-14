from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from apps.user.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'alias', 'avatar')


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'bg-blue-500', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'bg-blue-500', 'placeholder': 'Contraseña'}))
