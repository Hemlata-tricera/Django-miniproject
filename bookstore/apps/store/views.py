from django.shortcuts import render
from django.http import HttpResponse
from .models import Book


# Create your views here.
def homepage(request):
    title_query = request.GET.get('title', '')  # Get title search query from URL parameters
    author_query = request.GET.get('author', '')  # Get author search query from URL parameters
    books = Book.objects.all()  # Simple search

    if title_query:
        # Filter books by title
        books = books.filter(
            title__icontains=title_query)

    if author_query:
        books = books.filter(
            author__icontains=author_query)

    return render(request, 'homepage.html', {'title_query': title_query, 'author_query':author_query, 'books': books})
