from django.db import models


# Create your models here.
class Sell(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', help_text='30%-70% скидка на все')
    is_active = models.BooleanField(verbose_name='На главную', default=False)
    image = models.ImageField(upload_to='Sell/%Y/%m/%d', verbose_name='Фото', blank=True, null=True)
    is_pub = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'


class Reclame(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание', help_text='Максимум 254 символ!')
    is_active = models.BooleanField(verbose_name='На главную', default=False)
    image = models.ImageField(upload_to='Hello/%Y/%m/%d', verbose_name='Фото', help_text='1920*1001')
    is_pub = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Реклама'
        verbose_name_plural = 'Рекламы'


class Address(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', help_text='Пушкина 46/3')
    is_active = models.BooleanField(verbose_name='На главную', default=False)
    image = models.ImageField(upload_to='Address/%Y/%m/%d', verbose_name='Фото')
    map_place = models.URLField(verbose_name='Ссылка на карту')
    email = models.EmailField(verbose_name='Эл. адрес')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')
    is_pub = models.DateTimeField(verbose_name='Дата', auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class AboutUs(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    is_active = models.BooleanField(verbose_name='Пред', default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Инфо'
        verbose_name_plural = 'О нас'


class Team(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    image = models.ImageField(upload_to='Team/%Y/%m/%d', verbose_name='Фото')
    description = models.TextField(verbose_name='Описание')
    site = models.URLField(max_length=200, verbose_name='Ссылка на соц сеть')
    POSITION = (
        ('DIRECTOR', 'Директор'),
        ('MANAGER', 'Менеджер'),
        ('ADMINISTRATOR', 'Администратор'),
        ('DESIGNER', 'Дизайнер'),
        ('SELLER', 'Продавец'),
    )
    position = models.CharField(max_length=50, choices=POSITION, default='WEB DEVELOPER', verbose_name='Позиция')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Член команды'
        verbose_name_plural = 'Команда'


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Эл.Адрес')
    subject = models.CharField(max_length=100, verbose_name='Причина')
    message = models.TextField(verbose_name='Текст')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

