from django.db import models
from refers.models import Genre
from refers.models import PublishingHouse
from refers.models import TypeCover
from refers.models import Author
from refers.models import Serie

def image_folder(instance,filename): #instanse - объект - Book
    filename = instance.slug + '.' + filename.split('.')[1]
    return '{0}/{1}'.format(instance.slug, filename) #return f'books/{instanse.pk}-{filename}'

class Book(models.Model):
    #id/pk = auto increment
    name = models.CharField(
        max_length=200, 
        verbose_name="Наименование")
    description = models.TextField(
        max_length=3000, 
        verbose_name="Описание", 
        blank=True, 
        null=True)
    tag = models.CharField(
        max_length=1000, 
        verbose_name="Тэги для поиска", 
        blank=True, 
        null=True)
    slug = models.SlugField(verbose_name="Slug")
    cover = models.ImageField(upload_to=image_folder, verbose_name="Обложка", null = True, blank = True) #upload_to = 'books/'
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена, BYN")
    author = models.ForeignKey(
        Author,
        verbose_name="Автор",
        related_name = "books",
        on_delete=models.PROTECT)
    serie = models.ForeignKey(
        Serie,
        verbose_name="Серия",
        #on_delete=models.CASCADE удалится жанр, удалится вся книга (тк они связаны)
        #on_delete=models.DO_NOTHING удалится жанр, поле останется пустым для книги
        on_delete=models.PROTECT)#если захотят удалить жанр, будет сопротивляться удалению
    genre = models.ManyToManyField(
        Genre,
        verbose_name="Жанр")
    year = models.IntegerField(verbose_name="Год издания")
    page = models.IntegerField(verbose_name="Количество страниц")
    type_cover = models.ForeignKey(
        TypeCover,
        verbose_name="Переплёт",
        on_delete=models.PROTECT)
    book_format = models.CharField(max_length=50, verbose_name="Формат")
    book_ISBN = models.CharField(max_length=50, verbose_name="ISBN")
    weight_gram = models.IntegerField(verbose_name="Вес, гр")
    age_restrictions = models.CharField(max_length=50, verbose_name="Возрастные ограничения")
    publishing_house = models.ForeignKey(
        PublishingHouse,
        verbose_name="Издательство",
        on_delete=models.PROTECT) #если захотят удалить издательство, будет сопротивляться удалению
    quantity_for_sale = models.IntegerField(verbose_name="Количество книг в наличии")
    available = models.BooleanField(default=True, verbose_name="Доступно к заказу")
    rating = models.FloatField(verbose_name="Рейтинг")
    created = models.DateTimeField( #date type DateField or DateTimeField
        auto_now=False,
        auto_now_add=True,
        verbose_name="Дата создания")
    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name="Дата последнего изменения")
    objects = models.Manager()

    def get_absolute_url(self):
        return f'/book/{self.pk}/'

    def __str__(self):
        return self.name

class Journal(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    number = models.IntegerField(verbose_name="Выпуск")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена, BYN")
    month = models.CharField(max_length=50, verbose_name="Месяц")
    year = models.IntegerField(verbose_name="Год издания")
    page = models.IntegerField(verbose_name="Количество страниц")
    available = models.BooleanField(default=True, verbose_name="Доступно к заказу")
    created = models.DateTimeField( #date type DateField or DateTimeField
        auto_now=False,
        auto_now_add=True,
        verbose_name="Дата создания")
    updated = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name="Дата последнего изменения")
    
    def get_absolute_url(self):
        return f'/journal/{self.pk}/'

    def __str__(self):
        return self.name