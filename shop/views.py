from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Author, Genre, Reader, Librarian

#CRUD ДЛЯ КНИГ
class BookListView(ListView):
    model = Book
    template_name = 'shop/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    template_name = 'shop/book_detail.html'
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'year', 'description', 'cover', 'author', 'genre', 'publisher']
    template_name = 'shop/book_form.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'year', 'description', 'cover', 'author', 'genre', 'publisher']
    template_name = 'shop/book_form.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'shop/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

#CRUD ДЛЯ СОТРУДНИКОВ
class LibrarianListView(ListView):
    model = Librarian
    template_name = 'shop/librarian_list.html'
    context_object_name = 'librarians'

class LibrarianDetailView(DetailView):
    model = Librarian
    template_name = 'shop/librarian_detail.html'
    context_object_name = 'librarian'

class LibrarianCreateView(CreateView):
    model = Librarian
    fields = ['name', 'position', 'photo']
    template_name = 'shop/librarian_form.html'
    success_url = reverse_lazy('librarian_list')

class LibrarianUpdateView(UpdateView):
    model = Librarian
    fields = ['name', 'position', 'photo']
    template_name = 'shop/librarian_form.html'
    success_url = reverse_lazy('librarian_list')

class LibrarianDeleteView(DeleteView):
    model = Librarian
    template_name = 'shop/librarian_confirm_delete.html'
    success_url = reverse_lazy('librarian_list')

#АВТОРЫ
class AuthorListView(ListView):
    model = Author
    template_name = 'shop/simple_list.html'
    context_object_name = 'object_list'
    extra_context = {'title': 'Авторы'}

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'shop/simple_detail.html'
    context_object_name = 'object'

class AuthorCreateView(CreateView):
    model = Author
    fields = ['first_name', 'last_name', 'biography']
    template_name = 'shop/simple_form.html'
    success_url = reverse_lazy('author_list')

class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'biography']
    template_name = 'shop/simple_form.html'
    success_url = reverse_lazy('author_list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'shop/simple_confirm_delete.html'
    success_url = reverse_lazy('author_list')

#ЖАНРЫ
class GenreListView(ListView):
    model = Genre
    template_name = 'shop/simple_list.html'
    context_object_name = 'object_list'
    extra_context = {'title': 'Жанры'}

class GenreDetailView(DetailView):
    model = Genre
    template_name = 'shop/simple_detail.html'
    context_object_name = 'object'

class GenreCreateView(CreateView):
    model = Genre
    fields = ['name']
    template_name = 'shop/simple_form.html'
    success_url = reverse_lazy('genre_list')

class GenreUpdateView(UpdateView):
    model = Genre
    fields = ['name']
    template_name = 'shop/simple_form.html'
    success_url = reverse_lazy('genre_list')

class GenreDeleteView(DeleteView):
    model = Genre
    template_name = 'shop/simple_confirm_delete.html'
    success_url = reverse_lazy('genre_list')

#ЧИТАТЕЛИ
class ReaderListView(ListView):
    model = Reader
    template_name = 'shop/simple_list.html'
    context_object_name = 'object_list'
    extra_context = {'title': 'Читатели'}

class ReaderDetailView(DetailView):
    model = Reader
    template_name = 'shop/simple_detail.html'
    context_object_name = 'object'

class ReaderCreateView(CreateView):
    model = Reader
    fields = ['first_name', 'last_name', 'ticket_number', 'faculty']
    template_name = 'shop/simple_form.html'
    success_url = reverse_lazy('reader_list')

class ReaderUpdateView(UpdateView):
    model = Reader
    fields = ['first_name', 'last_name', 'ticket_number', 'faculty']
    template_name = 'shop/simple_form.html'
    success_url = reverse_lazy('reader_list')

class ReaderDeleteView(DeleteView):
    model = Reader
    template_name = 'shop/simple_confirm_delete.html'
    success_url = reverse_lazy('reader_list')