from django.db import models
from apps.users.models import ClientProfile
import datetime


def year_choices():
    return [(y, y) for y in range(1980, datetime.date.today().year + 1)]


def current_year():
    return datetime.date.today().year


class BrandModel(models.Model):
    brand = models.CharField(max_length=100,
                             verbose_name='Марка',
                             help_text='Введите название производителя авто (марка)',
                             )
    model = models.CharField(max_length=100,
                             verbose_name='Модель',
                             help_text='Введите модель авто',
                             )

    def __str__(self):
        return '{} {}'.format(self.brand, self.model)

    class Meta:
        verbose_name_plural = "Марки-модели"


class Car(models.Model):
    client = models.ForeignKey(ClientProfile,
                               null=True,
                               on_delete=models.CASCADE,
                               verbose_name='Владелец',
                               help_text='выберете владельца авто',
                               related_name='car_client',
                               blank=True,
                               )

    brand_model = models.ForeignKey(BrandModel,
                                    on_delete=models.CASCADE,
                                    verbose_name='Марка-модель',
                                    related_name='car_brandmodel',
                                    )

    year_manufacturing = models.IntegerField(verbose_name='год выпуска',
                                             choices=year_choices(),
                                             default=current_year(),
                                             )
    vin = models.CharField(max_length=100,
                           verbose_name='vin-code',
                           help_text='Введите vin',
                           blank=True
                           )

    car_number = models.CharField(max_length=100,
                                  verbose_name='Гос.номер',
                                  help_text='Введите гос.номер авто',
                                  blank=True
                                  )
    other_char = models.CharField(max_length=100,
                                  verbose_name='Другие характеристики',
                                  help_text='Введите дополнительную информацию об авто ( цвет, особенности frgg и т.д.)',
                                  blank=True
                                  )

    def __str__(self):
        return '{} {} г/н {} {}'.format(self.brand_model, self.year_manufacturing, self.car_number, self.other_char)

    class Meta:
        verbose_name_plural = "Машины"
