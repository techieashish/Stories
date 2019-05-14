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
class ProfileForm(forms.Form):

    class Meta:
        model = Profile
        fields = "__all__"

class ResourcesForm(forms.Form):

    class Meta:
        model = Resources
        fields = "__all__"

