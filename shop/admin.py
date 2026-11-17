from django.contrib import admin
from .models import Author, Genre, Publisher, Book, Reader, Librarian, Loan, Review

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Reader)
admin.site.register(Librarian)
admin.site.register(Loan)
admin.site.register(Review)