"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from book.views import AuthorList,list_books,BookDetail,AuthorDetail,list_books,review_books,review_book,add_author
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', list_books,name="books"),
    # url(r'^books/$', BookList.as_view()),
    url(r'^authors/$', AuthorList.as_view(),name="authors"),
    url(r'^books/(?P<pk>|[-\w]+)/$', BookDetail.as_view(),name="book-detail"),
    url(r'^authors/(?P<pk>|[-\w]+)/$', AuthorDetail.as_view(),name='author-detail'),
    url(r'^review/$', review_books, name='review-books'),
    url(r'^review/(?P<pk>[-\w]+)/$', review_book, name='review-book'),
    url(r'^add-author/$', add_author, name='add-author'),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

