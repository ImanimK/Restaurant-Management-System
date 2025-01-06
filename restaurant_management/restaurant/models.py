from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# ✅ Custom User Model
class CustomUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_staff_member = models.BooleanField(default=False)

# ✅ Menu Item Model
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

# ✅ Order Model (NO `customer_name` field)
class Order(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Ensure quantity has a default
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.menu_item.name}"

# ✅ Receipt Model
class Receipt(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    generated_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Receipt for Order {self.order.id}"

