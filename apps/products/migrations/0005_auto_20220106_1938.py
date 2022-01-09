# Generated by Django 2.2.24 on 2022-01-06 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20211124_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oil',
            name='container',
            field=models.ForeignKey(help_text='Выберите тару, в которой поступило масло', on_delete=django.db.models.deletion.CASCADE, related_name='oil', to='products.OilContainer', verbose_name='Тара'),
        ),
    ]