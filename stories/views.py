from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import Login, Registration, ProfileForm, ResourcesForm
from .models import Profile, Resources

# Create your views here.

def index(request):
    return redirect("story:login")


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
    return redirect('story:login')


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
        return redirect('story:create')
    return render(request, 'register.html', {'form': form})

@login_required(login_url="story:login")
def user_dashboard(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'dash.html', {'profile': profile})

@login_required(login_url="story:login")
def create_profile(request):
    form = ProfileForm(request.POST or None, request.FILES or None, request.GET or None)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('story:dash')
    return render(request, 'profile.html', {'form': form})


def edit_profile(request):
    profile_details = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile_details)
    if request.POST:
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            return redirect('music:dash')
    return render(request, 'profile.html', {'form': form, 'detail': profile_details})

@login_required(login_url="story:login")
def add_resource(request):
    form = ResourcesForm(request.POST or None)
    if form.is_valid():
        new_resource = form.save(commit=False)
        new_resource.user = request.user
        new_resource.save()
        return redirect("story:resources")
    return render(request, "add_resource.html", {"form": form})

@login_required(login_url="story:login")
def resources_dashboard(request):
    if not request.user.is_authenticated():
        return redirect('music:login')
    else:
        user_resources = request.user.resources.all()
        return render(request, 'resources.html', {'resources': user_resources})


def edit_resource(request, resource_id):
    resource = get_object_or_404(Resources, pk=resource_id)
    form = ResourcesForm(request.POST or None, instance=resource)
    if form.is_valid():
        modified_resource = form.save(commit=False)
        modified_resource.user = request.user
        modified_resource.save()
        return redirect("story:resource", resource_id=resource_id)
    return render(request, "edit_resource.html", {"form": form, "resource": resource})



def delete_resource(request, resource_id):
    selected_album = get_object_or_404(Resources, pk=resource_id)
    selected_album.delete()
    return redirect('story:resources_dashboard')