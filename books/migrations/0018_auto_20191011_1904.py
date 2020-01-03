# Generated by Django 2.2.5 on 2019-10-11 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refers', '0008_auto_20191011_1536'),
        ('books', '0017_auto_20191011_1807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(to='refers.Genre', verbose_name='Жанр'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='serie',
        ),
        migrations.AddField(
            model_name='book',
            name='serie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='refers.Serie', verbose_name='Серия'),
            preserve_default=False,
        ),
    ]
