from django.contrib import admin

from .models import Author, Book


class BookInline(admin.StackedInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline,]

    # Register models


admin.site.register(Author,AuthorAdmin )
admin.site.register(Book)