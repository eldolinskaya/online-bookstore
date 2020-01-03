from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from cart.models import BookInCart, Cart
from books.models import Book
#from django.contrib.auth.models import User
from cart.forms import BookInCartForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

User = get_user_model()

class AddToCartUpdateView(UpdateView):
    model = BookInCart
    form_class = BookInCartForm
    template_name = 'cart/add_to_cart.html'
    success_url = '/cart/list/' 
    def get_object(self):
        book_to_add = self.kwargs.get('pk')
        #if exists
        cart_id = self.request.session.get('cart_id')
        if not cart_id:
            if self.request.user.is_anonymous:
                user = User.objects.get(pk=11)
                cart = Cart.objects.create(user=user)
                self.request.session['cart_id'] = cart.pk
            else:
                user = self.request.user
                cart = Cart.objects.create(user=self.request.user)
                self.request.session['cart_id'] = cart.pk
        else:
            cart = Cart.objects.get(pk=cart_id)
        book = Book.objects.get(pk=book_to_add)
        book_in_cart, created = BookInCart.objects.get_or_create(
            book = book,
            cart = cart,
            defaults={'price': book.price}
        )
        if not created:
            book_in_cart.price = book.price * book_in_cart.quantity
            book_in_cart.quantity = book_in_cart.quantity + 1
            book_in_cart.save()
        return book_in_cart

    def form_valid(self, form, **kwargs):
        quantity = form.cleaned_data.get('quantity')
        price = self.object.book.price
        total_price = quantity * price
        self.object.price = total_price
        #self.object.save() -  использовать если не работает без предварительного сохранения
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CartListView(TemplateView):
    model = Cart
    template_name = "cart/list.html"
    #success_url = '/order/checkout/' 
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart_id = self.request.session.get('cart_id')
        cart = None
        if cart_id:
            cart = Cart.objects.get(pk=cart_id)
        context['cart'] = cart
        context['title'] = 'Корзина для заказа'
        context['action'] = 'Пожалуйста, проверьте Ваш заказ'
        return context