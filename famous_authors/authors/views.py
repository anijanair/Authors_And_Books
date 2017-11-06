from django.shortcuts import render, get_object_or_404

from .models import Author, Book

# Create views here.


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'authors/author_detail.html', {'author':author})

def book_detail(request, author_pk, book_pk):
    book = get_object_or_404(Book, author_id=author_pk, pk=book_pk)
    return render(request, 'authors/book_detail.html', {'book':book})

