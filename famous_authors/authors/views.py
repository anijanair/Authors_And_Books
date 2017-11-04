from django.http import HttpResponse
from django.shortcuts import render
from .models import Author

# Create views here.

def author_list(request):
    authors = Author.objects.all()
    output = ', '.join([str(author) for author in authors])
    return HttpResponse(output)