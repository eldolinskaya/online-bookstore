# Generated by Django 2.2.5 on 2019-09-29 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refers', '0002_publishinghouse'),
        ('books', '0008_auto_20190930_0112'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publishing_house',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='refers.PublishingHouse'),
            preserve_default=False,
        ),
    ]
