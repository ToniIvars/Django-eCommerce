from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.http import HttpResponse

from .forms import ProfileForm, ProductForm, BuyForm
from .models import Product, Order

import json

# Create your views here.
@login_required
def index(request):
    last_products = Product.objects.exclude(seller=User.objects.get(id=request.user.id)).order_by('-id')[:8]
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

            messages.success(request, 'Profile edited successfully')
            return redirect('index')

    else:
        form = ProfileForm(user_id=request.user.id)

    return render(request, 'store/profile.html', {'form':form})

@login_required
def view_profile(request, profile):
    if profile == request.user.username:
        return redirect('profile')

    info = get_object_or_404(User, username=profile)
    username = info.username

    products = Product.objects.filter(seller__exact=info.id)

    return render(request, 'store/view-profile.html', {'username':username, 'products':products})

@login_required
def product(request, product_name):
    product = get_object_or_404(Product, name=product_name)

    if str(product.seller) == request.user.username:
        return redirect('edit_product', product_name=product_name)
    
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

    if str(prod.seller) != request.user.username:
        messages.error(request, "Here are the products you can edit")
        return redirect('my_products')

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

    if str(prod.seller) != request.user.username:
        messages.error(request, "Here are the products you can delete")
        return redirect('my_products')

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
    
    else:
        query = request.POST.get('query')
    
    results = Product.objects.filter(name__icontains=query).exclude(seller=User.objects.get(id=request.user.id))
    
    results_ascendant = results.order_by('price')
    results_descendant = results.order_by('-price')

    return render(request, 'store/search.html', {'query':query, 'results_ascendant':results_ascendant, 'results_descendant':results_descendant})

@login_required
def buy(request, product_name):
    prod = get_object_or_404(Product, name=product_name)

    if str(prod.seller) == request.user.username:
        messages.error(request, "You can't buy your own product")
        return redirect('index')

    if request.method == 'POST':
        form = BuyForm(request.POST)
        
        if form.is_valid():
            address = form.cleaned_data['address']
            buyer = User.objects.get(id=request.user.id)
            quantity = form.cleaned_data['quantity']

            try:
                actual_order = Order.objects.get(product=prod, buyer=buyer, state='Opened')
                actual_order.quantity += quantity
                actual_order.save()

            except:
                Order(product=prod, buyer=buyer, address=address, state='Opened', quantity=quantity).save()

            messages.success(request, 'Product bought successfully')
            return redirect('index')

    else:
        form = BuyForm()

    return render(request, 'store/buy.html', {'product':prod.name, 'form':form})

@login_required
def orders(request):
    orders = Order.objects.filter(product__seller=User.objects.get(id=request.user.id)).order_by('date')
    products_state = None
    
    if orders:
        products = [order.product for order in orders]
        states = [order.state for order in orders]
        quantities = [order.quantity for order in orders]
        dates = [order.date for order in orders]

        products_state = tuple(zip(products, states, quantities, dates))

    return render(request, 'store/orders.html', {'products_state':products_state})

@login_required
def add_to_cart(request, product_name):
    prod = get_object_or_404(Product, name=product_name)

    if str(prod.seller) == request.user.username:
        messages.error(request, "You can't add to cart your own product")
        return redirect('index')

    if request.session.get('cart', None):
        cart = request.session['cart']

        if product_name in [prod['product'] for prod in request.session['cart']]:
            for i in range(len(cart)):
                if cart[i]['product'] == product_name:
                    cart[i]['quantity'] += 1
                    break 
        else:
            cart.append({'product':product_name, 'quantity':1})

        request.session['cart'] = cart

    else:
        request.session['cart'] = [
            {'product':product_name, 'quantity':1}
        ]

    messages.success(request, 'Product added to the cart')
    return redirect('product', product_name=product_name)

@login_required
def cart(request):
    cart = request.session.get('cart', None)
    cart_products = None
    if cart:        
        products = [Product.objects.get(name=prod['product']) for prod in cart]
        quantity = [prod['quantity'] for prod in cart]

        cart_products = set(zip(products, quantity))

    return render(request, 'store/cart.html', {'cart_products':cart_products})

@login_required
@require_POST
def change_quantity(request):
    cart = request.session['cart']
    post_data = json.loads(request.body.decode("utf-8"))
    
    if post_data['change'] == 'remove':
        for i in range(len(cart)):
            if cart[i]['product'] == post_data['product']:
                cart[i]['quantity'] -= 1
                new_quantity = cart[i]['quantity']
                break
    
    elif post_data['change'] == 'add':
        for i in range(len(cart)):
            if cart[i]['product'] == post_data['product']:
                cart[i]['quantity'] += 1
                new_quantity = cart[i]['quantity']
                break
                    
    request.session['cart'] = cart

    return HttpResponse(content=json.dumps({'new_quantity':new_quantity}), content_type = "application/json")

@login_required
@require_POST
def delete_from_cart(request):
    cart = request.session['cart']
    product_to_delete = json.loads(request.body.decode("utf-8"))['product_to_delete']

    for i in range(len(cart)):
        if cart[i]['product'] == product_to_delete:
            cart.pop(i)
            break
    
    request.session['cart'] = cart

    return HttpResponse(content=f'{product_to_delete} deleted form the cart', content_type = "application/json")