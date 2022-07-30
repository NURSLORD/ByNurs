
from django.db import models

from product.models import Product


class MyUser(models.Model):
    username = models.CharField(max_length=100, verbose_name="Имя", unique=True)
    email = models.EmailField(verbose_name='Эл.Адрес')
    cart = models.ManyToManyField(to=Product, related_name='cart', verbose_name='Корзина', blank=True)
    wishlist = models.ManyToManyField(to=Product, related_name='wishlist', verbose_name='Избранное', blank=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

