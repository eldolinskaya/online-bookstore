from django.contrib import admin
from . models import Book, Journal
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'slug',
        'cover',
        'price',
        'author',
        'serie',
        #'genre',
        'year',
        'page',
        'type_cover',
        'book_format',
        'book_ISBN',
        'weight_gram',
        'age_restrictions',
        'publishing_house',
        'quantity_for_sale',
        'available',
        'rating',
        'created',
        'updated'
    ]

class JournalAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'number',
        'price',
        'month',
        'year',
        'page',
        'available',
        'created',
        'updated'
    ]

admin.site.register(Book, BookAdmin)
admin.site.register(Journal, JournalAdmin)
