from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import Login, Registration, ProfileForm, ResourcesForm
from .models import Profile, Resources

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

def user_dashboard(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'dash.html', {'profile': profile})


def create_profile(request):
    if not request.user.is_authenticated():
        redirect('story:login')
    else:
        form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('story:dash')
        return render(request, 'profile.html', {'form': form})

