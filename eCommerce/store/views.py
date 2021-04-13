from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import ProfileForm
from .models import Product

# Create your views here.
@login_required
def index(request):
    last_products = Product.objects.all()
    return render(request, 'store/index.html', {'products':last_products})

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        
        if form.is_valid():
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            user = User.objects.get(id=request.user.id)

            if password:
                user.set_password(password)
            if email:
                user.email = email
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            
            user.save()

            messages.success(request, 'Profile edited successfully.')
            return redirect('index')

    else:
        form = ProfileForm(user_id=request.user.id)

    return render(request, 'store/profile.html', {'form':form, 'profile':True})