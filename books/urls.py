"""onlinestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from books.views import JournalHome, JournalDetailView, JournalListView, JournalCreateView, JournalUpdateView, JournalDeleteView
from books.views import BookHome, BookDetailView, BookListView, BookCreateView, BookUpdateView, BookDeleteView, HomePageView, SearchView
from django.conf.urls.static import static

urlpatterns = [
    path('book/', BookHome.as_view(), name='book-home'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='select-book'),
    path('book/list/', BookListView.as_view(), name='book-list'),
    path('book/create/', BookCreateView.as_view(), name='create-book'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='update-book'),
    path('book/delete/<int:pk>/', BookDeleteView.as_view(), name='delete-book'),
    path('journal/', JournalHome.as_view(), name='journal-home'),
    path('journal/<int:pk>/', JournalDetailView.as_view(), name='select-journal'),
    path('journal/list/', JournalListView.as_view(), name='journal-list'),
    path('journal/create/', JournalCreateView.as_view(), name='create-journal'),
    path('journal/update/<int:pk>/', JournalUpdateView.as_view(), name='update-journal'),
    path('journal/delete/<int:pk>/', JournalDeleteView.as_view(), name='delete-journal'),
    path('home/', HomePageView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search'),
]