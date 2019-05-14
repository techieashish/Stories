__author__ = 'ASHISH'
from django import forms
from django.contrib.auth.admin import User
from .models import Profile, Resources

class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class Registration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ("user", )

class ResourcesForm(forms.ModelForm):

    class Meta:
        model = Resources
        exclude = ("user", )

