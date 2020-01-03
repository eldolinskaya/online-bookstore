from django.contrib import admin
from . models import Genre
from . models import Author
from . models import Serie
from . models import PublishingHouse
from . models import TypeCover

# Register your models here.
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Serie)
admin.site.register(PublishingHouse)
admin.site.register(TypeCover)