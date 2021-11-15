from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class ClientProfile(models.Model):
    user = models.OneToOneField(User,
                                null=True,
                                on_delete=models.CASCADE,
                                related_name='profile',
                                blank=True
                                )
    name = models.CharField(max_length=100,
                            verbose_name='Имя',
                            help_text='Введите имя клиента',
                            blank=True
                            )
    phone = PhoneNumberField(verbose_name='телефон', help_text='введите номер телефона в формате +380671234567')

    def __str__(self):
        return '{} тел.{}'.format(self.name, self.phone)

    class Meta:
        verbose_name_plural = 'Клиенты'
