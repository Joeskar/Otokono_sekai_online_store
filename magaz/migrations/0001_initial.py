# Generated by Django 4.1.3 on 2022-12-07 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Названия категории')),
                ('slug', models.SlugField(max_length=100, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Названия')),
                ('slug', models.SlugField(max_length=100, verbose_name='URL')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Цена')),
                ('create_at', models.TimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликована')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='magaz.category', verbose_name='Категория')),
            ],
        ),
    ]
