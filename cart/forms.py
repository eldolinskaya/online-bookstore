from django.forms import ModelForm
from cart.models import BookInCart

class BookInCartForm(ModelForm):
    class Meta:
        model = BookInCart
        fields = [
            #'book',
            #'cart',
            'quantity',
            #'price',
        ]