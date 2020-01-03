from django.db import models
from django.contrib.auth import get_user_model
from books.models import Book
# Create your models here.
User = get_user_model()

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name = "Клиент",
        related_name = "carts",
        on_delete = models.PROTECT)
    objects = models.Manager()
    
    def total_price(self):
        books = self.books.all()
        total = 0
        for book in books:
            total += book.price
        return total

class BookInCart(models.Model):
    book = models.ForeignKey(
        Book,
        verbose_name = "Книга",
        related_name = "books_in_carts",
        on_delete = models.PROTECT
    )
    cart = models.ForeignKey(
        Cart, 
        verbose_name = "Корзина", 
        related_name = "books", 
        on_delete = models.PROTECT
    )
    quantity = models.IntegerField(
        verbose_name = "Количество", 
        default=1
    )
    price = models.DecimalField(
        verbose_name = "Цена, BYN", 
        max_digits=10, 
        decimal_places=2
    )
    objects = models.Manager()

    def __str__(self):
        return f"{self.book.name} * {self.quantity} шт."
