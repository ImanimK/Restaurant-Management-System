from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import CustomUser, MenuItem, Order, Receipt
from .forms import OrderForm, MenuItemForm

# ✅ Signup View
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto login after signup
            return redirect('dashboard')  # Redirect to dashboard after signup
    else:
        form = UserCreationForm()
    return render(request, 'restaurant/signup.html', {'form': form})

# ✅ Home View (Redirects Based on Role)
def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'restaurant/home.html')

# ✅ Dashboard View (Redirects to Manager or Staff)
@login_required
def dashboard(request):
    if request.user.is_manager:
        return redirect('manager_dashboard')
    return redirect('staff_dashboard')

# ✅ Manager Dashboard View (Restrict Access)
@login_required
def manager_dashboard(request):
    if not request.user.is_manager:
        return redirect('staff_dashboard')
    menu_items = MenuItem.objects.all()
    orders = Order.objects.all()
    return render(request, 'restaurant/manager_dashboard.html', {'menu_items': menu_items, 'orders': orders})

# ✅ Staff Dashboard View
@login_required
def staff_dashboard(request):
    orders = Order.objects.filter(created_by=request.user)
    return render(request, 'restaurant/staff_dashboard.html', {'orders': orders})

# ✅ Create Order View (Fix IntegrityError)
@login_required
def create_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.created_by = request.user  # Assign the logged-in user
            order.save()
            return redirect('staff_dashboard')
    else:
        form = OrderForm()
    return render(request, 'restaurant/create_order.html', {'form': form})

# ✅ Add Menu Item View (Managers Only) (Fix NoReverseMatch)
@login_required
def add_menu_item(request):
    if not request.user.is_manager:
        return redirect('staff_dashboard')
    if request.method == "POST":
        form = MenuItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manager_dashboard')
    else:
        form = MenuItemForm()
    return render(request, 'restaurant/add_menu_item.html', {'form': form})

# ✅ Cancel Order View (Managers Only)
@login_required
def cancel_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.user.is_manager:
        order.status = "Cancelled"
        order.save()
    return redirect('manager_dashboard')

# ✅ Update Order Status View
@login_required
def update_order_status(request, order_id, status):
    """ Allows manager to update order status """
    if not request.user.is_manager:
        return redirect('staff_dashboard')

    order = get_object_or_404(Order, id=order_id)
    if status in ["Pending", "In Progress", "Completed", "Cancelled"]:
        order.status = status
        order.save()
    return redirect('manager_dashboard')

# ✅ Generat Receipt View (Fix Missing Function)
@login_required
def generate_receipt(request, order_id):
    """ Generate a receipt for the given order """
    order = get_object_or_404(Order, id=order_id)
    receipt, created = Receipt.objects.get_or_create(order=order)
    return render(request, 'restaurant/receipt.html', {'receipt': receipt})

# ✅ Print Receipt View (Fix NoReverseMatch)
@login_required
def print_receipt(request, order_id):
    """ Print receipt for an order """
    order = get_object_or_404(Order, id=order_id)
    receipt, created = Receipt.objects.get_or_create(order=order)
    return render(request, 'restaurant/receipt.html', {'receipt': receipt})

