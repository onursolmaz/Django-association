from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, FileInput

from home.models import UserProfile


class SearchForm(forms.Form):
    query = forms.CharField(label="Search", max_length=100)


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

        widgets = {
            "username": TextInput(attrs={"class": "input form-control", "placeholder": "username"}),
            "email": TextInput(attrs={"class": "input form-control", "placeholder": "e-mail"}),
            "first_name": TextInput(attrs={"class": "input form-control", "placeholder": "first name"}),
            "last_name": TextInput(attrs={"class": "input form-control", "placeholder": "last name"})
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["image"]
        widgets = {
            "image": FileInput(attrs={"class": "input form-control", "placeholder": "image"})
        }
