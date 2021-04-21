from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from .forms import ProfileForm, ProductForm
from .models import Product

# Create your views here.
@login_required
def index(request):
    last_products = Product.objects.all().order_by('-id')[:8]
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

    return render(request, 'store/profile.html', {'form':form})

@login_required
def view_profile(request, profile):
    info = get_object_or_404(User, username=profile)
    username = info.username

    products = Product.objects.all().filter(seller__exact=info.id)

    return render(request, 'store/view-profile.html', {'username':username, 'products':products})

@login_required
def product(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    
    return render(request, 'store/product.html', {'product':product})

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        
        if form.is_valid():
            prod = form.save(commit=False)
            prod.seller = User.objects.get(id=request.user.id)
            prod.save()

            messages.success(request, 'Product created successfully')
            return redirect('index')

    else:
        form = ProductForm()

    return render(request, 'store/create-product.html', {'form':form})

@login_required
def edit_product(request, product_name):
    prod = get_object_or_404(Product, name=product_name)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=prod)
        
        if form.is_valid():
            prod = form.save(commit=False)
            prod.seller = User.objects.get(id=request.user.id)
            prod.save()

            messages.success(request, 'Product edited successfully')
            return redirect('index')

    else:
        form = ProductForm(instance=prod)

    return render(request, 'store/edit-product.html', {'form':form})

@login_required
def delete_product(request, product_name):
    prod = get_object_or_404(Product, name=product_name)

    if request.method == 'POST':
        if request.POST.get('delete'):
            prod.delete()

            messages.success(request, 'Product deleted successfully')
        
        return redirect('index')

    return render(request, 'store/delete-product.html', {'product':prod.name})

@login_required
def my_products(request):
    products = Product.objects.filter(seller__exact=request.user.id)

    return render(request, 'store/my-products.html', {'products':products})

@login_required
def search(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')
        if not query:
            messages.error(request, 'You must specify a query in the search URL')
            return redirect('index')

        results = Product.objects.filter(name__icontains=query)
        url_filter = request.GET.get('f', False)
    
    else:
        query = request.POST.get('query')
        results = Product.objects.filter(name__icontains=query)
        url_filter = False

    return render(request, 'store/search.html', {'results':results, 'query':query, 'filter':url_filter})

@login_required
def buy(request, product_name):
    prod = get_object_or_404(Product, name=product_name)

    return render(request, 'store/buy.html', {'product':prod.name})