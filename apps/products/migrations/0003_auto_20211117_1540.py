# Generated by Django 2.2.24 on 2021-11-17 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211117_1515'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kitservice',
            options={'verbose_name_plural': 'Услуги (набор работ)'},
        ),
        migrations.AlterField(
            model_name='detail',
            name='detail_manufacturer',
            field=models.CharField(help_text='Введите название поставщика детали', max_length=100, verbose_name='производитель детали'),
        ),
        migrations.AlterField(
            model_name='kitservice',
            name='in_price',
            field=models.PositiveIntegerField(default=0, help_text='Поле заполнится автоматически', verbose_name='Себестоимость грн.'),
        ),
    ]
