from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, "main.html")

