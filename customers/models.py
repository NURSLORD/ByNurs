from django.db import models

from product.models import Product


class MyUser(models.Model):
    username = models.CharField(max_length=100, verbose_name="Имя пользователя", unique=True)
    email = models.EmailField(verbose_name='Эл.Адрес')
    full_name = models.CharField(max_length=100, verbose_name='Имя', null=True, blank=True)
    phone_number = models.CharField(max_length=100, verbose_name='Номер телефона', null=True, blank=True)
    image = models.ImageField(upload_to='Customer/%Y/%m/%d', verbose_name="Фото", default='Customer/2022/08/26/default-avatar-profile-icon-vector-social-media-user-photo-183042379.jpg')
    cart = models.ManyToManyField(to=Product, related_name='cart', verbose_name='Корзина', blank=True)
    wishlist = models.ManyToManyField(to=Product, related_name='wishlist', verbose_name='Избранное', blank=True)

    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Order(models.Model):
    FEE = [
        ('CASH', 'Наличка'),
        ('CARD', 'Карта'),
    ]
    customer = models.ForeignKey(to=MyUser, on_delete=models.CASCADE, verbose_name='Клиент')
    fee = models.CharField(verbose_name='Платеж', choices=FEE, default='CARD', max_length=4)
    service = models.BooleanField(verbose_name='Доставка', default=True)
    address = models.CharField(verbose_name='Адрес', max_length=80)
    total_item = models.PositiveIntegerField(verbose_name='Сумма', default=1)
    ord_date = models.DateTimeField(verbose_name='Дата заказа', auto_now_add=True)
    discount = models.IntegerField(verbose_name='Скидка', default=0)
    invoice_number = models.PositiveBigIntegerField(verbose_name='Номер счета', blank=True, null=True)

    def __str__(self):
        return f'{self.customer}'

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class ItemOrders(models.Model):
    product = models.ForeignKey(Product, models.SET_NULL, null=True, verbose_name='Продукт')
    quantity = models.IntegerField(verbose_name='Кол-во', default=1)
    price = models.PositiveIntegerField(verbose_name='Цена', blank=True, null=True)
    discount = models.IntegerField(verbose_name='Скидка', default=0)
    order = models.ForeignKey(Order, models.SET_NULL, null=True, blank=True, verbose_name='Заказчик',
                              related_name='orders')

    def __str__(self):
        return f'{self.order}'

    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'


class Statistics(models.Model):
    amount_products = models.PositiveIntegerField(verbose_name='Кол-во продуктов', blank=True, null=True)
    amount_categories = models.PositiveIntegerField(verbose_name='Кол-во категорий', blank=True, null=True)
    amount_sub_categories = models.PositiveIntegerField(verbose_name='Кол-во саб категорий', blank=True, null=True)
    amount_customers = models.PositiveIntegerField(verbose_name='Кол-во клиентов', blank=True, null=True)
    amount_blogs = models.PositiveIntegerField(verbose_name='Кол-во блогов', blank=True, null=True)
    amount_comments = models.PositiveIntegerField(verbose_name='Кол-во комметариев', blank=True, null=True)
