from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, DeletionMixin
from .forms import AuthorCreateForm, GenreCreateForm, SerieCreateForm, PublishingHouseCreateForm, TypeCoverCreateForm
from .models import Author, Genre, Serie, PublishingHouse, TypeCover
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

#АВТОРЫ
class AuthorHome(TemplateView):
    template_name = 'author/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AuthorDetailView(DetailView):
    model = Author

class AuthorListView(ListView):
    model = Author
    template_name = 'author/list.html'

class AuthorCreateView(PermissionRequiredMixin, CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'author/create.html'
    permission_required='refers.add_author'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Создание нового объекта:"
        return context

class AuthorUpdateView(PermissionRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorCreateForm 
    template_name = 'author/create.html'
    permission_required='refers.change_author'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Редактирование объекта:"
        return context

class AuthorDeleteView(PermissionRequiredMixin, DeleteView):
    model = Author
    template_name = 'author/delete.html'
    success_url = '/author/list/'
    permission_required='refers.delete_author'

#ЖАНРЫ
class GenreHome(TemplateView):
    template_name = 'genre/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GenreDetailView(DetailView):
    model = Genre

class GenreListView(ListView):
    model = Genre
    template_name = 'genre/list.html'


class GenreCreateView(PermissionRequiredMixin, CreateView):
    model = Genre
    form_class = GenreCreateForm
    template_name = 'genre/create.html'
    permission_required='refers.add_genre'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Создание нового объекта:"
        return context

class GenreUpdateView(PermissionRequiredMixin, UpdateView):
    model = Genre
    form_class = GenreCreateForm 
    template_name = 'genre/create.html'
    permission_required='refers.change_genre'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Редактирование объекта:"
        return context

class GenreDeleteView(PermissionRequiredMixin, DeleteView):
    model = Genre
    template_name = 'genre/delete.html'
    success_url = '/genre/list/'
    permission_required='refers.delete_genre'

#СЕРИЯ
class SerieHome(TemplateView):
    template_name = 'serie/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SerieDetailView(DetailView):
    model = Serie

class SerieListView(ListView):
    model = Serie
    template_name = 'serie/list.html'

class SerieCreateView(PermissionRequiredMixin, CreateView):
    model = Serie
    form_class = SerieCreateForm
    template_name = 'serie/create.html'
    permission_required='refers.add_serie'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Создание нового объекта:"
        return context

class SerieUpdateView(PermissionRequiredMixin, UpdateView):
    model = Serie
    form_class = SerieCreateForm 
    template_name = 'serie/create.html'
    permission_required='refers.change_serie' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Редактирование объекта:"
        return context

class SerieDeleteView(PermissionRequiredMixin, DeleteView):
    model = Serie
    template_name = 'serie/delete.html'
    success_url = '/serie/list/'
    permission_required='refers.delete_serie'

#ИЗДАТЕЛЬСТВО
class PublishingHouseHome(TemplateView):
    template_name = 'publishing-house/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PublishingHouseDetailView(DetailView):
    model = PublishingHouse

class PublishingHouseListView(ListView):
    model = PublishingHouse
    template_name = 'publishing-house/list.html'

class PublishingHouseCreateView(PermissionRequiredMixin, CreateView):
    model = PublishingHouse
    form_class = PublishingHouseCreateForm
    template_name = 'publishing-house/create.html'
    permission_required='refers.add_publishing_house'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Создание нового объекта:"
        return context

class PublishingHouseUpdateView(PermissionRequiredMixin, UpdateView):
    model = PublishingHouse
    form_class = PublishingHouseCreateForm 
    template_name = 'publishing-house/create.html'
    permission_required='refers.change_publishing_house' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Редактирование объекта:"
        return context

class PublishingHouseDeleteView(PermissionRequiredMixin, DeleteView):
    model = PublishingHouse
    template_name = 'publishing-house/delete.html'
    success_url = '/publishing-house/list/'
    permission_required='refers.delete_publishing_house'

#ПЕРЕПЛЁТ
class TypeCoverHome(TemplateView):
    template_name = 'type-cover/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TypeCoverDetailView(DetailView):
    model = TypeCover

class TypeCoverListView(ListView):
    model = TypeCover
    template_name = 'type-cover/list.html'

class TypeCoverCreateView(PermissionRequiredMixin, CreateView):
    model = TypeCover
    form_class = TypeCoverCreateForm
    template_name = 'type-cover/create.html'
    permission_required='refers.add_type_cover'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Создание нового объекта:"
        return context

class TypeCoverUpdateView(PermissionRequiredMixin, UpdateView):
    model = TypeCover
    form_class = TypeCoverCreateForm 
    template_name = 'type-cover/create.html'
    permission_required='refers.change_type_cover'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Редактирование объекта:"
        return context

class TypeCoverDeleteView(PermissionRequiredMixin, DeleteView):
    model = TypeCover
    template_name = 'type-cover/delete.html'
    success_url = '/type-cover/list/'
    permission_required='refers.delete_type_cover'