from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', cache_page(60)(homepage), name='home'),
    path('categories/', cache_page(60)(shop), name='shop'),
    path('product-page/', cache_page(60)(productpage), name='productpage'),
    path('check-out/', checkout, name='check-out'),
    path('contact/', cache_page(60)(Contact.as_view()), name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('shopping-cart/', cart, name='shopping-cart')
]
