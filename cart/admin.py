from django.contrib import admin
from . models import Cart, BookInCart
# Register your models here.

class BookInCartAdmin(admin.ModelAdmin):
    list_display = [
        'book',
        'cart',
        'quantity',
        'price',
    ]

admin.site.register(Cart)
admin.site.register(BookInCart, BookInCartAdmin)