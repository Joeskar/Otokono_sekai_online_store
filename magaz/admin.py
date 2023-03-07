from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'digital', 'slug', 'show_image')
    prepopulated_fields = {'slug': ('name',)}

    def show_image(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    show_image.__name__ = 'Картинка'


admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

admin.site.site_title = 'Админ-панель сайта о интернет магазине'
admin.site.site_header = 'Админ-панель сайта о интернет магазине'
