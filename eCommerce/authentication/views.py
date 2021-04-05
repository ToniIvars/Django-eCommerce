from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(f'Logged in as {user}')
        else:
            messages.error(request, 'The username or the password are incorrect.')

    return render(request, 'authentication/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')