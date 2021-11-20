# Generated by Django 2.2.24 on 2021-11-20 17:41

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OilContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_date', models.DateField(default=datetime.date.today, help_text='Выберите дату', verbose_name='Дата поступления на склад')),
                ('volume', models.CharField(choices=[('1л', '1л'), ('2л', '2л'), ('5л', '5л'), ('10л', '10л'), ('20л', '20л')], help_text='Выберите объём тары', max_length=100, null=True, verbose_name='Объём тары')),
            ],
            options={
                'verbose_name_plural': 'Фасовка масла',
            },
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(help_text='Введите названия продукта', max_length=100, verbose_name='Название')),
                ('in_price', models.PositiveIntegerField(default=0, help_text='Введите цену от поставщика продукта', verbose_name='Себестоимость грн.')),
                ('extra_charge', models.PositiveIntegerField(default=25, help_text='Введите сколько % необходимо добавить к себестоимости продукта', verbose_name='Наценка %')),
                ('out_price', models.PositiveIntegerField(default=0, help_text='Введите цену для клиента продукта', verbose_name='Стоимость грн.')),
                ('part_number_original', models.CharField(help_text='Введите № детали по каталогу оригинального производителя ', max_length=100, verbose_name='№ детали оригинал')),
                ('part_manufacturer', models.CharField(help_text='Введите название поставщика детали', max_length=100, verbose_name='производитель детали')),
                ('part_number_cross', models.CharField(blank=True, help_text='Введите № детали по "заменителю"', max_length=100, null=True, verbose_name='cross № детали')),
                ('part_provider', models.CharField(help_text='Введите название поставщика детали', max_length=100, verbose_name='поставщик детали')),
                ('stock', models.PositiveIntegerField(default=1, help_text='Введите количество деталей', verbose_name='кол-во')),
                ('is_available', models.BooleanField(default=False, help_text='для добавления детали на склад поставьте галочку', verbose_name='на склад')),
            ],
            options={
                'verbose_name_plural': 'Детали',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(help_text='Введите названия работы', max_length=100, null=True, verbose_name='Название')),
                ('work_our', models.PositiveIntegerField(default=1, help_text='Введите количество н.часов (AV, 1 = 5мин)', verbose_name='н.часы (AV)')),
            ],
            options={
                'verbose_name_plural': 'Услуги (работы)',
            },
        ),
        migrations.CreateModel(
            name='Oil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(help_text='Введите названия продукта', max_length=100, verbose_name='Название')),
                ('in_price', models.PositiveIntegerField(default=0, help_text='Введите цену от поставщика продукта', verbose_name='Себестоимость грн.')),
                ('extra_charge', models.PositiveIntegerField(default=25, help_text='Введите сколько % необходимо добавить к себестоимости продукта', verbose_name='Наценка %')),
                ('out_price', models.PositiveIntegerField(default=0, help_text='Введите цену для клиента продукта', verbose_name='Стоимость грн.')),
                ('stock_l', models.DecimalField(decimal_places=2, default=1, help_text='Введите количество л', max_digits=12, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='кол-во')),
                ('is_available', models.BooleanField(default=False, help_text='для добавления масла на склад поставьте галочку', verbose_name='на склад')),
                ('container', models.OneToOneField(help_text='Выберите тару, в которой поступило масло', on_delete=django.db.models.deletion.CASCADE, related_name='oil', to='products.OilContainer', verbose_name='Тара')),
            ],
            options={
                'verbose_name_plural': 'Масло',
            },
        ),
        migrations.CreateModel(
            name='KitService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(help_text='Введите названия работы', max_length=100, null=True, verbose_name='Название')),
                ('work_our', models.PositiveIntegerField(default=1, help_text='Введите количество н.часов (AV, 1 = 5мин)', verbose_name='н.часы (AV)')),
                ('services', models.ManyToManyField(help_text='Выберите работы из которых состоит услуга', related_name='kit_service', to='products.Work', verbose_name='набор работ')),
            ],
            options={
                'verbose_name_plural': 'Услуги (набор работ)',
            },
        ),
    ]
