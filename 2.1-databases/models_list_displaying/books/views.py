from math import ceil

from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_all = list(Book.objects.all())
    books = [books_all[idx * 3:idx * 3 + 3] for idx in range(ceil(len(books_all) / 3))]
    context = {
        "books": books
    }
    return render(request, template, context)


def date_view(request, pub_date):
    pass
