from django.db import models
from datetime import date
from apps.cars.models import Car
from apps.products.models import Part, Oil, Work, KitService


class WorkOrder(models.Model):
    open_date = models.DateField(default=date.today,
                                 verbose_name='Дата открытия ЗН',
                                 help_text='Выберите дату')

    close_date = models.DateField(null=True,
                                  verbose_name='Дата закрытия ЗН',
                                  help_text='Выберите дату',
                                  blank=True)

    car = models.ForeignKey(Car,
                            on_delete=models.CASCADE,
                            related_name='work_order',
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
                                              verbose_name='Общая сумма грн.',
                                              help_text='Поле зааполнится автоматически',
                                              )
    status_choices = [
        ('in_work', 'в работе'),
        ('completed', 'закрыт'),
    ]
    status = models.CharField(max_length=20,
                              choices=status_choices,
                              default='in_work',
                              verbose_name='Статус ЗН'
                              )

    is_paid = models.BooleanField(default=False,
                                  verbose_name='Оплата'
                                  )

    comment = models.TextField(max_length=500,
                               verbose_name='Комментарии',
                               blank=True)

    @property
    def is_editable(self):
        if self.status == 'in_work' and self.is_paid is False:
            return True
        else:
            return False

    def __str__(self):
        return 'ЗН от {} по авто {} {} на сумму {}'.format(self.open_date, self.car, self.get_status_display(),
                                                           self.total_price)

    class Meta:
        verbose_name_plural = 'Заказ-Наряды'


class WorOrderItem(models.Model):
    work_order = models.ForeignKey(WorkOrder,
                                   on_delete=models.CASCADE,
                                   verbose_name='ЗН',
                                   related_name='work_order_item',
                                   help_text='Выберите ЗН',
                                   )
    part = models.ForeignKey(Part,
                             null=True,
                             on_delete=models.CASCADE,
                             verbose_name='ЗЧ',
                             related_name='work_order_item_part',
                             help_text='Выберите ЗЧ использованную по ЗН',
                             blank=True
                             )
    oil = models.ForeignKey(Oil,
                            null=True,
                            on_delete=models.CASCADE,
                            verbose_name='масло',
                            related_name='work_order_item_oil',
                            help_text='Выберите масло использованное по ЗН',
                            blank=True
                            )
    service = models.ForeignKey(Work,
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name='работа',
                                related_name='work_order_item_service',
                                help_text='Выберите работу по ЗН',
                                blank=True
                                )
    kit_service = models.ForeignKey(KitService,
                                    null=True,
                                    on_delete=models.CASCADE,
                                    verbose_name='набор работ',
                                    related_name='work_order_item_kit_service',
                                    help_text='Выберите работу(набор работ) по ЗН',
                                    blank=True
                                    )

    class Meta:
        verbose_name_plural = 'Позиции в ЗН'
