from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ProfileForm

# Create your views here.
@login_required
def index(request):
    return render(request, 'store/index.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            messages.success(request, 'Profile edited successfully.')
            return redirect('index')

    else:
        form = ProfileForm(user_id=request.user.id)

    return render(request, 'store/profile.html', {'form':form})