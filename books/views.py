from django.shortcuts import render
from .models import Book

# Create your views here.
def books(request):
    books = Book.objects
    return render(request, 'books/books.html', {'books': books})
