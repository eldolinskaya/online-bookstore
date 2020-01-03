from django.forms import ModelForm
from books.models import Book, Journal

class BookCreateForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name', 
            'slug', 
            'cover', 
            'price', 
            'author', 
            'serie', 
            'genre', 
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
            'description',
            'tag',
        ]
 
class JournalCreateForm(ModelForm):
    class Meta:
        model = Journal
        fields = [
        'name',
        'number',
        'price',
        'month',
        'year',
        'page',
        'available',
        ]