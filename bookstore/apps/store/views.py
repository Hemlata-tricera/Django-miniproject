from django.shortcuts import render
from django.http import HttpResponse

from .models import Book, Cart, CartItem
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.db.models import Q


# Create your views here.
def homepage(request):
    title_query = request.GET.get('title', '')  # Get title search query from URL parameters
    author_query = request.GET.get('author', '')  # Get author search query from URL parameters
    # books = Book.objects.all()[:5]  # Simple search
    books = Book.objects.all() # Simple search

    if title_query and author_query:
        books = Book.objects.filter(Q(title__icontains=title_query) | Q(author__icontains=author_query))
        # Filter books by title
        # books = books.filter(
            # title__icontains=title_query) | books.filter(author__icontains=author_query)
        # books = books.filter(
        #     Q(title__icontains=title_query) | Q(author__icontains=author_query))
    # elif title_query:
    #     # Filter books by title
    #     books = books.filter(
    #         title__icontains=title_query)
    #
    # elif author_query:
    #     books = books.filter(
    #         author__icontains=author_query)

    return render(request, 'homepage.html', {'title_query': title_query, 'author_query': author_query, 'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})


def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart_id = request.session.get('cart_id')
    if not cart_id:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
    else:
        cart = get_object_or_404(Cart, id=cart_id)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('store:cart_detail')


def update_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    if request.method == 'POST':
        cart_item.quantity = int(request.POST.get('quantity', 1))
        cart_item.save()
    return redirect('store:cart_detail')


def cart_detail(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:
        return render(request, 'cart_detail.html', {'cart': None, 'total_price': 0})

    cart = get_object_or_404(Cart, id=cart_id)
    total_price = sum(item.total_price() for item in cart.cartitem_set.all())

    return render(request, 'cart_detail.html', {'cart': cart, 'total_price': total_price})


def remove_from_cart(request, book_id):
    cart_id = request.session.get('cart_id')
    cart = get_object_or_404(Cart, id=cart_id)
    cart_item = get_object_or_404(CartItem, cart=cart, book_id=book_id)
    cart_item.delete()
    return redirect('store:cart_detail')


