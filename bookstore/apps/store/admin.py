from django.contrib import admin
from .models import Category, Book, CartItem, Cart

# Register your models here.
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(CartItem)