"""
URL configuration for restaurant_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from orders import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_restaurant/', views.add_restaurant, name='add_restaurant'),
    path('add_branch/', views.add_branch, name='add_branch'),
    path('add_menu_item/', views.add_menu_item, name='add_menu_item'),
    path('view_restaurants/', views.view_restaurants, name='view_restaurants'),
    path('view_menu_items/<int:branch_id>/', views.view_menu_items, name='view_menu_items'),
    path('place_order/<int:menu_item_id>/', views.place_order, name='place_order'),
    path('order_confirmation/<int:order_id>/', views.order_confirmation, name='order_confirmation'),
    path('view_orders/', views.view_orders, name='view_orders'),
    path('manage_order/<int:order_id>/', views.manage_order, name='manage_order'),
    path('rate_order/<int:order_id>/', views.rate_order, name='rate_order'),
    ]
