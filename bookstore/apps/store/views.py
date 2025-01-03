from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# Create your views here.
def homepage(request):
    query = request.GET.get('query', '')  # Get search query from URL parameters
    books = Book.objects.all()  # Simple search

    if query:
        # Filter books by title, author, or price
        books = books.filter(
            title__icontains=query) | books.filter(
            author__icontains=query) | books.filter(
            price__icontains=query)


    return render(request, 'homepage.html', {'query': query, 'books': books})
