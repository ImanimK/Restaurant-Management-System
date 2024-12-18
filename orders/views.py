from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .models import User, Restaurant, Branch, MenuItem, Order, Rating
from .forms import (UserRegisterForm, RestaurantForm, BranchForm,
                    MenuItemForm, OrderForm, RatingForm,UserLoginForm)


def index(request):
    return render(request, 'orders/index.html')

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')
    else:
        form = UserLoginForm()
    return render(request, 'orders/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'orders/register.html', {'form': form})


def dashboard(request):
    if request.user.is_restaurant_manager:
        return render(request, 'orders/restaurant_dashboard.html')
    elif request.user.is_branch_manager:
        return render(request, 'orders/branch_dashboard.html')
    elif request.user.is_deliveryman:
        return render(request, 'orders/deliveryman_dashboard.html')
    else:
        return render(request, 'orders/customer_dashboard.html')


def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.owner = request.user
            restaurant.save()
            return redirect('dashboard')
    else:
        form = RestaurantForm()
    return render(request, 'orders/add_restaurant.html', {'form': form})


def add_branch(request):
    if request.method == 'POST':
        form = BranchForm(request.POST)
        if form.is_valid():
            branch = form.save(commit=False)
            branch.restaurant = request.user.restaurant
            branch.save()
            return redirect('dashboard')
    else:
        form = BranchForm()
    return render(request, 'orders/add_branch.html', {'form': form})


def add_menu_item(request):
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            menu_item = form.save(commit=False)
            menu_item.branch = request.user.branch
            menu_item.save()
            return redirect('dashboard')
    else:
        form = MenuItemForm()
    return render(request, 'orders/add_menu_item.html', {'form': form})


def view_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render(request,
                  'orders/view_restaurants.html',
                  {'restaurants': restaurants})


def view_menu_items(request, branch_id):
    branch = get_object_or_404(Branch, id=branch_id)
    menu_items = MenuItem.objects.filter(branch=branch)
    return render(request, 'orders/view_menu_items.html',
                  {'branch': branch, 'menu_items': menu_items})


def place_order(request, menu_item_id):
    menu_item = get_object_or_404(MenuItem, id=menu_item_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = request.user
            order.menu_item = menu_item
            order.save()
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'orders/place_order.html',
                  {'form': form, 'menu_item': menu_item})


def order_confirmation(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_confirmation.html', {'order': order})


def view_orders(request):
    if request.user.is_restaurant_manager:
        orders = Order.objects.filter(
            menu_item__branch__restaurant__owner=request.user)
    elif request.user.is_branch_manager:
        orders = Order.objects.filter(menu_item__branch__manager=request.user)
    elif request.user.is_deliveryman:
        orders = Order.objects.filter(deliveryman=request.user)
    else:
        orders = Order.objects.filter(customer=request.user)
    return render(request, 'orders/view_orders.html', {'orders': orders})


def manage_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('view_orders')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/manage_order.html',
                  {'form': form, 'order': order})


def rate_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.order = order
            rating.customer = request.user
            rating.save()
            return redirect('view_orders')
    else:
        form = RatingForm()
    return render(request, 'orders/rate_order.html',
                  {'form': form, 'order': order})
