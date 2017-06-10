from pprint import pprint
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.db.models import Count
from .models import Author,Book
from .forms import Reviewform,BookForm
from django.views.generic import DetailView, View
from django.views.generic.edit import CreateView
from django.shortcuts import render,get_object_or_404,redirect
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


# Paste into Views.py - don't forget to import get_object_or_404!
def review_books(request):
    """
    List all of the books that we want to review.
    """
    books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')

    context = {
        'books': books,
    }

    return render(request, "list-to-review.html", context)


def review_book(request, pk):
    """
    Review an individual book
    """
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = Reviewform(request.POST)
        if form.is_valid():
            book.is_favourite = form.cleaned_data['is_favourite'];
            book.review = form.cleaned_data['review'];
            if not book.reviewed_by:
                book.reviewed_by = request.user
            book.save()
            return redirect('review-books')
    else:
        form = Reviewform

    context = {
        'book': book,
        'form': form,
    }

    return render(request, "review-book.html", context)


def add_author(request):
    return HttpResponse('We could put anything here.')


class ReviewList(View):
    def get(self,request):
        books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')
        context = {
            'books': books,
            'form': BookForm,
        }
        return render(request, "list-to-review.html", context)

    def post(self,request):
        form = BookForm(request.POST)
        books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')
        if form.is_valid():
            form.save()
            return redirect('review-books')
        context = {
            'books': books,
            'form': form,
        }

        return render(request, "list-to-review.html", context)


class CreateAuthor(CreateView):
    model = Author
    fields = ['name',]
    template_name = '../templates/create-author.html'

    def get_success_url(self):
        return reverse('review-books')






