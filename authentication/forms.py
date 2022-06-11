import email
from pyexpat import model
from django import forms
from . import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    adresse_email  = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name')

    # pseudo = forms.CharField(max_length=20, required=True)
    # nom    = forms.CharField(max_length=50, required=True)
    # prenom = forms.CharField(max_length=50, required=True)
    # email  = forms.EmailField(widget=forms.EmailInput, validators=[validators.EmailValidator])
    # password = forms.CharField(max_length=20, widget=forms.PasswordInput)