# Generated by Django 2.2.24 on 2021-11-20 17:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Введите имя клиента', max_length=100, verbose_name='Имя')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(help_text='введите номер телефона в формате +380671234567', max_length=128, region=None, verbose_name='телефон')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
