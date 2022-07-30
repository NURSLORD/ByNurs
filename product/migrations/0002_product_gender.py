# Generated by Django 3.2.9 on 2022-07-29 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gender',
            field=models.CharField(choices=[('men', 'Мужские'), ('women', 'Женские'), ('baby', 'Детский'), ('universal', 'Унисекс')], default='universal', max_length=10, verbose_name='Пол'),
        ),
    ]
