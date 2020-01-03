from django.db import models

class Genre(models.Model):
    #id/pk = auto increment
    name = models.CharField(
        verbose_name="Жанр",
        help_text='Введите наименование жанра',
        max_length=100,
        blank=False, #blank и null сигнализирует django, может ли это поле оставаться пустым (если False,то не могут)
        null=False)
    descr = models.TextField(max_length=3000, verbose_name="Описание", blank=True, null=True)
    def get_absolute_url(self):
        return f'/genre/{self.pk}/'
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Автор", 
        help_text='Введите ФИО автора')
    descr = models.TextField(max_length=3000, verbose_name="Описание", blank=True, null=True)
    def get_absolute_url(self):
        return f'/author/{self.pk}/'
    def __str__(self):
        return self.name    

class Serie(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Серия",
        help_text='Введите наименование серии')
    descr = models.TextField(max_length=3000, verbose_name="Описание", blank=True, null=True)
    def get_absolute_url(self):
        return f'/serie/{self.pk}/'
    def __str__(self):
        return self.name    

class PublishingHouse(models.Model):
    name = models.CharField(
        max_length=200, 
        verbose_name="Издательство",
        help_text='Введите название издательства')
    descr = models.TextField(max_length=3000, verbose_name="Описание", blank=True, null=True)
    def get_absolute_url(self):
        return f'/publishing-house/{self.pk}/'
    def __str__(self):
        return self.name   

class TypeCover(models.Model):
    name = models.CharField(
        max_length=50, 
        verbose_name="Переплёт",
        help_text='Введите вид переплёта')
    descr = models.TextField(max_length=3000, verbose_name="Описание", blank=True, null=True)
    def get_absolute_url(self):
        return f'/type-cover/{self.pk}/'
    def __str__(self):
        return self.name