from .models import Book
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
