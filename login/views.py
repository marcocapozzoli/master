from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from login.models import User


def home(request):
    return render(request, 'login/home.html')

def login_view(request):
    if request == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home')) 
        else:
            return render(request, 'login/login.html', {
                "message" : "Invalid username and/or password."
            })
    else:
        return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'login/index.html')