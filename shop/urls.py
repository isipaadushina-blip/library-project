from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),

    # Книги
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),

    # Авторы
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('authors/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/update/', views.AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),

    # Жанры
    path('genres/', views.GenreListView.as_view(), name='genre_list'),
    path('genres/<int:pk>/', views.GenreDetailView.as_view(), name='genre_detail'),
    path('genres/create/', views.GenreCreateView.as_view(), name='genre_create'),
    path('genres/<int:pk>/update/', views.GenreUpdateView.as_view(), name='genre_update'),
    path('genres/<int:pk>/delete/', views.GenreDeleteView.as_view(), name='genre_delete'),

    # Читатели
    path('readers/', views.ReaderListView.as_view(), name='reader_list'),
    path('readers/<int:pk>/', views.ReaderDetailView.as_view(), name='reader_detail'),
    path('readers/create/', views.ReaderCreateView.as_view(), name='reader_create'),
    path('readers/<int:pk>/update/', views.ReaderUpdateView.as_view(), name='reader_update'),
    path('readers/<int:pk>/delete/', views.ReaderDeleteView.as_view(), name='reader_delete'),

    # Сотрудники
    path('librarians/', views.LibrarianListView.as_view(), name='librarian_list'),
    path('librarians/<int:pk>/', views.LibrarianDetailView.as_view(), name='librarian_detail'),
    path('librarians/create/', views.LibrarianCreateView.as_view(), name='librarian_create'),
    path('librarians/<int:pk>/update/', views.LibrarianUpdateView.as_view(), name='librarian_update'),
    path('librarians/<int:pk>/delete/', views.LibrarianDeleteView.as_view(), name='librarian_delete'),
]