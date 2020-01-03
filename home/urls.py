from django.conf.urls import url
from home.views import register, ProfileListView, ProfileUpdateView, edit
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # post views
    path('register/', register, name='register'),
    path('account/', ProfileListView.as_view(), name='account'),
    path('account/update/', edit, name='account-update'),
]
