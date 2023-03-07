from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Пользователь')
    name = models.CharField(max_length=100, null=True, verbose_name='Имя пользователя')
    email = models.CharField(max_length=100, null=True, verbose_name='Емайл пользователя')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name='Названия продукта')
    slug = models.SlugField(max_length=100, verbose_name='URL')
    price = models.FloatField(verbose_name='Цена')
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Products(models.Model):
    """Продукты на странице"""
    name = models.CharField(max_length=100, verbose_name='Названия')
    status_of_product = models.CharField(blank=True, max_length=100, verbose_name='Статус продукта')
    slug = models.SlugField(max_length=100, verbose_name='URL')
    about = models.TextField(blank=True, verbose_name='О товаре')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    create_at = models.TimeField(auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликована')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'product_slug': self.slug})


class Category(models.Model):
    """Категория продуктов"""
    name = models.CharField(max_length=100, verbose_name='Названия категории')
    slug = models.SlugField(max_length=100, verbose_name='URL')

    def __str__(self):
        return self.name
