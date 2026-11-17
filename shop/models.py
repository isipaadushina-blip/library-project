from django.db import models

# 1. Автор
class Author(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    biography = models.TextField(blank=True, null=True, verbose_name="Биография")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

# 2. Жанр
class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название жанра")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

# 3. Издательство
class Publisher(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название издательства")
    city = models.CharField(max_length=100, verbose_name="Город")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Издательство"
        verbose_name_plural = "Издательства"

# 4. Книга (Главная таблица с картинкой обложки)
class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название книги")
    year = models.IntegerField(verbose_name="Год издания")
    description = models.TextField(blank=True, null=True, verbose_name="Аннотация")
    
    # Картинка №1 (Обложка)
    cover = models.ImageField(upload_to='covers/', verbose_name="Обложка книги", blank=True, null=True)
    
    # Связи
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Жанр")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name="Издательство")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

# 5. Читатель (Студент/Преподаватель)
class Reader(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    ticket_number = models.CharField(max_length=20, unique=True, verbose_name="Номер читательского билета")
    faculty = models.CharField(max_length=100, verbose_name="Факультет")

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.ticket_number})"

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

# 6. Сотрудник библиотеки (С картинкой)
class Librarian(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО Сотрудника")
    position = models.CharField(max_length=100, verbose_name="Должность")
    
    # Картинка №2 (Фото сотрудника)
    photo = models.ImageField(upload_to='librarians/', verbose_name="Фото сотрудника", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

# 7. Выдача книги
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name="Читатель")
    librarian = models.ForeignKey(Librarian, on_delete=models.SET_NULL, null=True, verbose_name="Выдал сотрудник")
    loan_date = models.DateField(auto_now_add=True, verbose_name="Дата выдачи")
    return_date = models.DateField(blank=True, null=True, verbose_name="Дата возврата")

    def __str__(self):
        return f"{self.book} -> {self.reader}"

    class Meta:
        verbose_name = "Выдача"
        verbose_name_plural = "Выдачи"

# 8. Отзыв на книгу
class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Книга")
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE, verbose_name="Читатель")
    text = models.TextField(verbose_name="Текст отзыва")
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name="Оценка (1-5)")

    def __str__(self):
        return f"Отзыв от {self.reader} на {self.book}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"