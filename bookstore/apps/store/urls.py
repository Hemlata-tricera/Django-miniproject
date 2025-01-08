from django.contrib import admin
from django.urls import path
from .views import *
from . import views
app_name = 'store'

urlpatterns = [
    path('', homepage, name='homepage'),
    # path('login/', login_page, name='login_page'),    # Login page
    # path('logout/', logout_page, name='logout_page'),    # Login page
    # path('register/', register_page, name='register'),  # Registration page
    path('book/<int:pk>/', book_detail, name='book_detail'), # For Book Detail
    path('add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('remove/<int:book_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('login/', login_page, name='login_page'),    # Login page
    path('logout/', logout_page, name='logout_page'),    # Login page
    path('register/', register_page, name='register'),  # Registration page


]