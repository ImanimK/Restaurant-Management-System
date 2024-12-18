from django import forms
from .models import User, Restaurant, Branch, MenuItem, Order, Rating
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'is_customer', 'is_restaurant_manager', 'is_branch_manager', 'is_deliveryman']
        widgets = {
            'password': forms.PasswordInput(),
        }

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'trade_license_no', 'address']

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['restaurant', 'name', 'address', 'manager']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price', 'restaurant']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['restaurant', 'branch', 'items', 'total_price', 'status', 'deliveryman']
        widgets = {
            'items': forms.CheckboxSelectMultiple(),
        }

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['customer_rating', 'deliveryman_rating', 'customer_comment', 'deliveryman_comment']
