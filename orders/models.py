from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_restaurant_manager = models.BooleanField(default=False)
    is_branch_manager = models.BooleanField(default=False)
    is_deliveryman = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name='orders_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='orders_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user',
    )

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    trade_license_no = models.CharField(max_length=100)
    address = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Branch(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Delivered', 'Delivered')], default='Pending')
    deliveryman = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='deliveries')

class Rating(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    customer_rating = models.IntegerField(null=True, blank=True)
    deliveryman_rating = models.IntegerField(null=True, blank=True)
    customer_comment = models.TextField(null=True, blank=True)
    deliveryman_comment = models.TextField(null=True, blank=True)
