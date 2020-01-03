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
from refers.views import AuthorHome, AuthorDetailView, AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView
from refers.views import GenreHome, GenreDetailView, GenreListView, GenreCreateView, GenreUpdateView, GenreDeleteView
from refers.views import SerieHome, SerieDetailView, SerieListView, SerieCreateView, SerieUpdateView, SerieDeleteView
from refers.views import PublishingHouseHome, PublishingHouseDetailView, PublishingHouseListView, PublishingHouseCreateView, PublishingHouseUpdateView, PublishingHouseDeleteView
from refers.views import TypeCoverHome, TypeCoverDetailView, TypeCoverListView, TypeCoverCreateView, TypeCoverUpdateView, TypeCoverDeleteView

urlpatterns = [
    path('genre/', GenreHome.as_view(), name='genre-home'),
    path('genre/<int:pk>/', GenreDetailView.as_view(), name='select-genre'),
    path('genre/list/', GenreListView.as_view(), name='genre-list'), #вставить потом в ссылку в шаблон
    path('genre/create/', GenreCreateView.as_view(), name='create-genre'),
    path('genre/update/<int:pk>/', GenreUpdateView.as_view(), name='update-genre'),
    path('genre/delete/<int:pk>/', GenreDeleteView.as_view(), name='delete-genre'),
    path('author/', AuthorHome.as_view(), name='author-home'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='select-author'),
    path('author/list/', AuthorListView.as_view(), name='author-list'),
    path('author/create/', AuthorCreateView.as_view(), name='create-author'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='update-author'),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view(), name='delete-author'),
    path('serie/', SerieHome.as_view(), name='serie-home'),
    path('serie/<int:pk>/', SerieDetailView.as_view(), name='select-serie'),
    path('serie/list/', SerieListView.as_view(), name='serie-list'),
    path('serie/create/', SerieCreateView.as_view(), name='create-serie'),
    path('serie/update/<int:pk>/', SerieUpdateView.as_view(), name='update-serie'),
    path('serie/delete/<int:pk>/', SerieDeleteView.as_view(), name='delete-serie'),
    path('publishing-house/', PublishingHouseHome.as_view(), name='publishing-house-home'),
    path('publishing-house/<int:pk>/', PublishingHouseDetailView.as_view(), name='select-publishing-house'),
    path('publishing-house/list/', PublishingHouseListView.as_view(), name='publishing-house-list'),
    path('publishing-house/create/', PublishingHouseCreateView.as_view(), name='create-publishing-house'),
    path('publishing-house/update/<int:pk>/', PublishingHouseUpdateView.as_view(), name='update-publishing-house'),
    path('publishing-house/delete/<int:pk>/', PublishingHouseDeleteView.as_view(), name='delete-publishing-house'),
    path('type-cover/', TypeCoverHome.as_view(), name='type-cover-home'),
    path('type-cover/<int:pk>/', TypeCoverDetailView.as_view(), name='select-type-cover'),
    path('type-cover/list/', TypeCoverListView.as_view(), name='type-cover-list'),
    path('type-cover/create/', TypeCoverCreateView.as_view(), name='create-type-cover'),
    path('type-cover/update/<int:pk>/', TypeCoverUpdateView.as_view(), name='update-type-cover'),
    path('type-cover/delete/<int:pk>/', TypeCoverDeleteView.as_view(), name='delete-type-cover'),
]
