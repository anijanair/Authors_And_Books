from django.shortcuts import render

from .models import Author

# Create views here.


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/author_list.html', {'authors': authors})

def auhtor_detail(request, pk):
    author = Author.objects.get(pk=pk)
    return render(request, 'authors/author_detail.html', {'author':author})
