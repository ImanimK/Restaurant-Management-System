from django.urls import path
from django.contrib.auth import views as auth_views  # ✅ Import Django's auth views
from . import views

urlpatterns = [
    # ✅ Home Page
    path('', views.home, name='home'),

    # ✅ Authentication Routes
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='restaurant/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # ✅ Dashboard Routes
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/manager/', views.manager_dashboard, name='manager_dashboard'),
    path('dashboard/staff/', views.staff_dashboard, name='staff_dashboard'),

    # ✅ Manager Actions (Fix NoReverseMatch for `add_menu_item`)
    path('menu/add/', views.add_menu_item, name='add_menu_item'),
    path('update_order/<int:order_id>/<str:status>/', views.update_order_status, name='update_order_status'),
    path('cancel_order/<int:order_id>/', views.cancel_order, name='cancel_order'),

    # ✅ Staff Actions
    path('order/create/', views.create_order, name='create_order'),

    # ✅ Receipt Actions (Fix NoReverseMatch for `print_receipt`)
    path('order/<int:order_id>/generate_receipt/', views.generate_receipt, name='generate_receipt'),
    path('order/<int:order_id>/print_receipt/', views.print_receipt, name='print_receipt'),  # ✅ Added
]

