# Generated by Django 4.1.3 on 2023-01-25 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magaz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='about',
            field=models.TextField(blank=True, verbose_name='О товаре'),
        ),
        migrations.AddField(
            model_name='products',
            name='status_of_product',
            field=models.CharField(blank=True, max_length=100, verbose_name='Статус продукта'),
        ),
    ]
