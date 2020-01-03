from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, DeletionMixin
from .forms import BookCreateForm, JournalCreateForm
from .models import Book, Journal
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q

#КНИГИ
class BookHome(TemplateView):
    template_name = 'book/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class BookDetailView(DetailView):
    model = Book

class BookListView(ListView):
    model = Book
    #pagenation
    template_name = 'book/list.html'

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookCreateForm
    template_name = 'book/create.html'
    permission_required='books.add_book'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Создание нового объекта:"
        return context

class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookCreateForm 
    template_name = 'book/create.html'
    permission_required='books.change_book'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Редактирование объекта:"
        return context

class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'book/delete.html'
    success_url = '/book/list/'
    permission_required='books.delete_book'

#ЖУРНАЛЫ
class JournalHome(TemplateView):
    template_name = 'journal/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class JournalDetailView(DetailView):
    model = Journal

class JournalListView(ListView):
    model = Journal
    template_name = 'journal/list.html'

class JournalCreateView(PermissionRequiredMixin, CreateView):
    model = Journal
    form_class = JournalCreateForm
    template_name = 'journal/create.html'
    permission_required='books.add_journal'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Создание нового объекта:"
        return context

class JournalUpdateView(PermissionRequiredMixin, UpdateView):
    model = Journal
    form_class = JournalCreateForm 
    template_name = 'journal/create.html'
    permission_required='books.change_journal'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = "Редактирование объекта:"
        return context

class JournalDeleteView(PermissionRequiredMixin, DeleteView):
    model = Journal
    template_name = 'journal/delete.html'
    success_url = '/journal/list/'
    permission_required='books.delete_journal'

#Главная страница
class HomePageView(ListView):
    model = Book
    form_class = BookCreateForm
    template_name = 'book/home_page.html'

#Поиск
class SearchView(View):
    template_name = 'book/search.html'
    model = Book
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('q')
        found = Book.objects.filter(
            Q(name__icontains=query)|
            Q(tag__icontains=query)
        )
        context = {
            'found':found
        }
        return render(self.request, self.template_name, context)