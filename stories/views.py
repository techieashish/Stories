from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import Login, Registration

# Create your views here.

def index(request):
    return render(request, "main.html")


def user_login(request):
    form = Login(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('')

    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('stories:login')


def user_registration(request):
    form = Registration(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('stories:create')
    return render(request, 'register.html', {'form': form})

