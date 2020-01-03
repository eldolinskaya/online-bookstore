from django.forms import ModelForm
from refers.models import Author, Genre, Serie, PublishingHouse, TypeCover

class GenreCreateForm(ModelForm):
    class Meta:
        model = Genre
        fields = ['name', 'descr']

class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'descr']

class SerieCreateForm(ModelForm):
    class Meta:
        model = Serie
        fields = ['name', 'descr']

class PublishingHouseCreateForm(ModelForm):
    class Meta:
        model = PublishingHouse
        fields = ['name', 'descr']

class TypeCoverCreateForm(ModelForm):
    class Meta:
        model = TypeCover
        fields = ['name', 'descr']