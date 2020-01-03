from django.shortcuts import render #, redirect
#from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from order.models import Order
from order.forms import OrderCreateForm
from cart.models import Cart
from order.utils import get_price
from django.core.mail import send_mail
#from django.contrib.auth import get_user_model
#User = get_user_model()

class OrderCreate(UpdateView):
    template_name = 'order/create.html'
    model = Order
    form_class = OrderCreateForm
    success_url = '/order/checkout/thanks'

    def get_object(self):
        order_id = self.request.session.get('order_id')
        cart_id = self.request.session.get('cart_id')
        #user_id = self.request.session.get('user_id')
        #если в сессии нет корзины
        #if not cart_id: 
        #    return HttpResponse('/order/checkout/')
        cart = Cart.objects.get(pk = cart_id)
        #user = User.objects.get(pk = user_id)
        order, created = Order.objects.get_or_create(
            cart = cart,
            price = get_price(cart.total_price())[0],
            delivery_price = get_price(cart.total_price())[1],
        )
        if created:
            self.request.session['order_id'] = order.pk
        return order

    def get_success_url(self):
        #user = self.request.user
        #self.object.user = user
        #self.object.save()
        # send mail() текущий юзер в self.request
        # можно сделать через signals - > берем post signals
        # если редактирование происходит из нескольких  мест, заказы появляются с другого источника ->надо влезть еще туда, 
        # т.е в каждом месте поставить перехватчик
        # сигналы можно прописать в модели , например pre-save -> перед сохранением в БД
        # оброботчик сигнала - функция
        # минус сигналов - нет self.request , те не достать текущего юзера и текущую сессию
        
        # Добавить отправку письма по email send_mail() self.request.user -> у меня не добавлен user в order -> OperationalError
        e_mail = self.object.e_mail
        title = 'Спасибо за покупку!'
        text = 'Уважаемый клиент! Ваш заказ уже обрабатывается нашими специалистами и будет доставлен согласно указанному Вами адресу/пункту самовывоза.'
        send_mail(title, text, 'bookstore.manager@yandex.ru', [e_mail])
        
        #удаляем корзину и заказ из сессии
        self.request.session['order_id'] = None
        self.request.session['cart_id'] = None
        return super().get_success_url()
    
class OrderDone(TemplateView):
    template_name = 'order/created.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context