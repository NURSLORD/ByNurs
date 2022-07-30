# Generated by Django 3.2.9 on 2022-07-27 14:27

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='Brand/%Y/%m/%d')),
                ('is_active', models.BooleanField(default=True, verbose_name='Пред')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='О категория')),
                ('is_active', models.BooleanField(default=True, verbose_name='Подтверждённый')),
                ('image', models.ImageField(upload_to='Category/%Y/%m/%d', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Название')),
                ('is_active', models.BooleanField(default=False, verbose_name='Популярный')),
                ('image', models.ImageField(upload_to='Sub/%Y/%m/%d', verbose_name='Фото')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_catis', to='product.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Под-категория',
                'verbose_name_plural': 'Под-категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='Название')),
                ('image_main', models.ImageField(blank=True, null=True, upload_to='Product/%Y/%m/%d', verbose_name='Полное фото')),
                ('image_right', models.ImageField(blank=True, null=True, upload_to='Product/%Y/%m/%d', verbose_name='Правое фото')),
                ('image_left', models.ImageField(blank=True, null=True, upload_to='Product/%Y/%m/%d', verbose_name='Левое фото')),
                ('description', models.TextField(verbose_name='Описание')),
                ('status', models.CharField(choices=[('sale', 'Скидка'), ('new', 'Новые'), ('just', 'Простые'), ('popular', 'Популярные')], default='just', max_length=10, verbose_name='Статус')),
                ('amount', models.PositiveIntegerField(default=1, verbose_name='Кол-во')),
                ('article', models.BigIntegerField(null=True, unique=True, verbose_name='Артикл')),
                ('old_price', models.PositiveIntegerField(default=0, verbose_name='Старая цена')),
                ('cur', models.CharField(choices=[('COM', 'сом'), ('USD', 'доллар'), ('RUB', 'руб')], default='C', max_length=3, verbose_name='Волюта')),
                ('new_price', models.IntegerField(blank=True, null=True, verbose_name='Новая цена')),
                ('pub_date', models.DateField(auto_now_add=True, null=True, verbose_name='Дата публикации')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_brand', to='product.brand', verbose_name='Бренд')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category', verbose_name='Категория')),
                ('sub_category', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, related_name='my_sub', to='product.subcategory', verbose_name='Под-категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
