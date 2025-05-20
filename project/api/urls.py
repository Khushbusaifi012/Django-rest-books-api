from django.urls import path
from .views import Booklist,Bookdetail,book_list

urlpatterns=[
    path('books/',Booklist.as_view(),name='book-list'),
    path('books/<int:pk>/',Bookdetail.as_view(),name='book-detail'),
    path('add-book/', book_list, name='book_list'),
]