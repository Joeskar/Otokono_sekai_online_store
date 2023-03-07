from .models import *

menu = [{'title': 'Главная страница', 'url_name': 'home'},
        {'title': 'Cтраница продукта', 'url_name': 'productpage'},
        {'title': 'Магазин', 'url_name': 'shop'},
        {'title': 'Информация о пользователе', 'url_name': 'check-out'}
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        products = Products.objects.all()
        context['menu'] = menu
        context['products'] = products

        return context
