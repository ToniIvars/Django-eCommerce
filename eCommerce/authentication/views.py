from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import LoginForm, SignupForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'The username or the password are incorrect.')
    
    elif request.user.is_authenticated:
        return redirect('index')

    else:
        form = LoginForm()

    return render(request, 'authentication/login.html', {'form':form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password == password2:
                # Creation of the user
                pass
            else:
                messages.error(request, 'Passwords must be equal')

    elif request.user.is_authenticated:
        return redirect('index')
    
    else:
        form = SignupForm()
        
    return render(request, 'authentication/signup.html', {'form':form})