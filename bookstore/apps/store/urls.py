from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/', login_page, name='login_page'),    # Login page
    path('logout/', logout_page, name='logout_page'),    # Login page
    path('register/', register_page, name='register'),  # Registration page
    # path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
]