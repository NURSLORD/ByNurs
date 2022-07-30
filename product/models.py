from django.db import models
from smart_selects.db_fields import ChainedForeignKey


# Create your models here.



class Brand(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='Brand/%Y/%m/%d')
    is_active = models.BooleanField(verbose_name='Пред', default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'


class Category(models.Model):
    title = models.CharField(max_length=80, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='О категория')
    is_active = models.BooleanField(verbose_name='Подтверждённый', default=True)
    image = models.ImageField(verbose_name='Фото', upload_to='Category/%Y/%m/%d')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SubCategory(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория',
                                 related_name='my_catis')
    title = models.CharField(max_length=80, verbose_name='Название')
    is_active = models.BooleanField(verbose_name='Популярный', default=False)
    image = models.ImageField(verbose_name='Фото', upload_to='Sub/%Y/%m/%d')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Под-категория'
        verbose_name_plural = 'Под-категории'


class Product(models.Model):
    COM = 'COM'
    USD = 'USD'
    RUB = 'RUB'
    C_U_R = [
        ('COM', 'сом'),
        ('USD', 'доллар'),
        ('RUB', 'руб'),
    ]
    FILTER = [
        ('sale', 'Скидка'),
        ('new', 'Новые'),
        ('just', 'Простые'),
        ('popular', 'Популярные'),
    ]
    GENDER = [
        ('men', 'Мужские'),
        ('women', 'Женские'),
        ('baby', 'Детский'),
        ('universal', 'Унисекс'),
    ]
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    sub_category = ChainedForeignKey(SubCategory, chained_field='category', chained_model_field='category',
                                     show_all=False,
                                     auto_choose=True,
                                     sort=True, verbose_name='Под-категория', related_name='my_sub')
    title = models.CharField(max_length=80, verbose_name='Название')
    image_main = models.ImageField(verbose_name='Полное фото', upload_to='Product/%Y/%m/%d', blank=True, null=True)
    image_right = models.ImageField(verbose_name='Правое фото', upload_to='Product/%Y/%m/%d', blank=True, null=True)
    image_left = models.ImageField(verbose_name='Левое фото', upload_to='Product/%Y/%m/%d', blank=True, null=True)
    brand = models.ForeignKey(to=Brand, verbose_name='Бренд', on_delete=models.SET_NULL, null=True,
                              related_name='my_brand')
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(verbose_name='Статус', choices=FILTER, max_length=10, default='just')
    gender = models.CharField(verbose_name='Пол', choices=GENDER, max_length=10, default='universal')
    amount = models.PositiveIntegerField(verbose_name='Кол-во', default=1)
    article = models.BigIntegerField(verbose_name='Артикл', unique=True, null=True)
    old_price = models.PositiveIntegerField(verbose_name='Старая цена', default=0)
    cur = models.CharField(verbose_name='Волюта', choices=C_U_R, default='C', max_length=3)
    new_price = models.IntegerField(verbose_name='Новая цена', null=True, blank=True)
    pub_date = models.DateField(verbose_name='Дата публикации', auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
