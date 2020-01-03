from django.contrib import admin
from django.urls import path
from order.views import  OrderCreate, OrderDone

app_name = 'order'
urlpatterns = [
    path('checkout/', OrderCreate.as_view(), name='create'),
    path('checkout/thanks', OrderDone.as_view(), name='created'),
]