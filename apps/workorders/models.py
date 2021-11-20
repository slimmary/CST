from django.db import models
from datetime import date
from apps.cars.models import Car


class Work_order(models.Model):
    open_date = models.DateField(default=date.today,
                                 verbose_name='Дата открытия ЗН',
                                 help_text='Выберите дату')

    close_date = models.DateField(null=True,
                                  verbose_name='Дата закрытия ЗН',
                                  help_text='Выберите дату',
                                  blank=True)

    car = models.ForeignKey(Car,
                            on_delete=models.CASCADE,
                            verbose_name='Автомобиль',
                            help_text='Выберите авто, на которое открыт ЗН',
                            )
    av_price = models.PositiveIntegerField(default=80,
                                           verbose_name='Цена нормачаса (AV) грн.',
                                           help_text='Введите цену ',
                                           )

    total_in_price_parts = models.PositiveIntegerField(default=0,
                                                       verbose_name='себестоимость за ЗЧ грн.',
                                                       help_text='Поле зааполнится автоматически',
                                                       )
    total_out_price_parts = models.PositiveIntegerField(default=0,
                                                        verbose_name='Стоимость ЗЧ для клиента грн.',
                                                        help_text='Поле зааполнится автоматически',
                                                        )
    total_price_services = models.PositiveIntegerField(default=0,
                                                       verbose_name='Стоимость работ грн.',
                                                       help_text='Поле зааполнится автоматически',
                                                       )
    total_price = models.PositiveIntegerField(default=0,
                                              verbose_name='СОбщая сумма грн.',
                                              help_text='Поле зааполнится автоматически',
                                              )
