# Generated by Django 2.2.5 on 2019-09-29 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refers', '0003_typecover'),
        ('books', '0009_book_publishing_house'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='type_cover',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='refers.TypeCover'),
            preserve_default=False,
        ),
    ]
