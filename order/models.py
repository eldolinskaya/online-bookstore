from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from home.models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    cart = models.ForeignKey(
        'cart.Cart',
        verbose_name = "Корзина",
        on_delete = models.PROTECT
    )
    price = models.DecimalField(
        verbose_name = "Цена, BYN", 
        max_digits=10, 
        decimal_places=2
    )
    delivery_price = models.DecimalField(
        verbose_name = "Цена доставки, BYN", 
        max_digits=10, 
        decimal_places=2
    )
    #user = models.ForeignKey(
    #    User,
    #    verbose_name = "Личные данные",
    #    null = True,
    #    blank = True,
    #    on_delete = models.PROTECT
    #)
    user_name = models.CharField(
        max_length=200,
        default = '',
        verbose_name = "ФИО получателя:", 
    )
    delivery_address = models.CharField(
        max_length=500, 
        verbose_name = "Адрес доставки:", 
    )
    mobile_number = models.CharField(
        max_length=50, 
        verbose_name = "Мобильный телефон:", 
    )
    e_mail = models.EmailField(verbose_name = "E-mail:")
    buying_type = models.CharField(
        max_length=50, 
        verbose_name = "Способ доставки:", 
        choices= (('Самовывоз', 'Самовывоз'),('Доставка', 'Доставка'))
    )
    comments = models.CharField(
        max_length=500,
        verbose_name = "Дополнительные комментарии:", 
        blank=True, 
        null=True
    )
    status = models.BooleanField(
        'Исполнен',
        default=False,
    )    
    created_date = models.DateTimeField( 
        auto_now=False,
        auto_now_add=True,
        verbose_name="Дата создания заказа")
    objects = models.Manager()

# их может быть несколько
#@receiver(pre_save, sender = Order)
#def order_updater(sender, instance, **kwargs):
    #default_name = User.objects.get()
    #instance.delivery_address = instance.delivery_address + 'datatime'
    #instance.user_name = instance.user_name
    #print(type(sender), sender, instance)
