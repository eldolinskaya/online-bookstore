# Generated by Django 2.2.5 on 2019-10-26 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0003_auto_20191026_1315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена, BYN')),
                ('delivery_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена доставки, BYN')),
                ('status', models.BooleanField(default=False, verbose_name='Исполнен')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cart.Cart', verbose_name='Корзина')),
            ],
        ),
    ]
