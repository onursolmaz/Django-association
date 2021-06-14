from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=100)


class singUpForm(UserCreationForm):
    username: forms.CharField(max_length=30, label="Username:")
    email = forms.EmailField(max_length=100, label="E mail :")
    first_name: forms.CharField(max_length=50, help_text="First name", label="First name:")
    last_name: forms.CharField(max_length=50, help_text="Last name", label="Last name:")

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
