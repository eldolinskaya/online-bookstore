from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'user_name',
        'buying_type',
        'delivery_address',
        'mobile_number',
        'e_mail',
        'created_date',
    ]

admin.site.register(Order, OrderAdmin)
