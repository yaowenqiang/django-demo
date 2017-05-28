from django.db.models import Count
from .models import Author,Book
from django.views.generic import DetailView, View
from django.shortcuts import render
# Create your views here.


def list_books(request):
    '''
    List books that had reviews
    '''
    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')
    # books = Book.objects.exclude(date_reviewed__isnull=True)

    context = {
        'books':books
    }
    # return HttpResponse('We could put anything here.')
    # return HttpResponse(request.user.username)
    return render(request, '../templates/list.html', context)


class AuthorList(View):
    def get(self, request):
        # authors = Author.objects.all()
        authors = Author.objects.annotate(
            published_books=Count('books')
        ).filter(
            published_books__gt=0
        )
        context = {
            'authors':authors
        }
        return render(request, '../templates/authors.html', context)


class BookDetail(DetailView):
    model = Book
    template_name = "../templates/book.html"


class AuthorDetail(DetailView):
    model = Author
    template_name = "../templates/author.html"
