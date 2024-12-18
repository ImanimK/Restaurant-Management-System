from django.contrib import admin
from .models import User, Restaurant, Branch, MenuItem, Order, Rating

admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Branch)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(Rating)
