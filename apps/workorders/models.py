from django.db import models
from datetime import date
from apps.cars.models import Car
from apps.products.models import Part, Oil, Work, KitService
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


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
                                                        verbose_name='Стоимость ЗЧ грн.',
                                                        help_text='Поле зааполнится автоматически',
                                                        )
    total_out_price_oil = models.PositiveIntegerField(default=0,
                                                      verbose_name='Стоимость масла грн.',
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

    def get_total_in_out_price_parts(self):
        total_in_price_parts = 0
        total_out_price_parts = 0
        for item in self.work_order_item.all():
            if item.part:
                total_in_price_parts += item.part.in_price
                total_out_price_parts += item.part.out_price
        self.total_in_price_parts = total_in_price_parts
        self.total_out_price_parts = total_out_price_parts
        return self.total_in_price_parts, self.total_out_price_parts

    def get_total_out_price_oil(self):
        for item in self.work_order_item.all():
            if item.oil:
                self.total_out_price_oil += item.oil.out_price
        return self.total_out_price_oil

    def get_total_price_services(self):
        list_services_in_kit_services = []
        for item in self.work_order_item.all():
            if item.kit_service:
                list_services_in_kit_services.append(item.kit_service.servicess.all())
                self.total_price_services += item.kit_service.work_our * self.av_price
            elif item.service:
                if item.servise not in list_services_in_kit_services:
                    self.total_price_services += item.service.work_our * self.av_price
        return self.total_price_services

    def get_total_price(self):
        self.total_price = self.total_out_price_parts + self.total_out_price_oil + self.total_price_services
        return self.total_price

    def save(self, *args, **kwargs):
        self.get_total_in_out_price_parts
        self.get_total_out_price_oil
        self.get_total_price_services
        self.get_total_price

        super(WorkOrder, self).save(*args, **kwargs)

    def __str__(self):
        return 'ЗН от {} по авто {} {} на сумму {}'.format(self.open_date, self.car, self.get_status_display(),
                                                           self.total_price)

    class Meta:
        verbose_name_plural = 'Заказ-Наряды'


class WorkOrderItem(models.Model):
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
                             help_text='Выберите ЗЧ, использованную по ЗН',
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
    amount = models.DecimalField(null=True,
                                 decimal_places=2,
                                 max_digits=12,
                                 default=1,
                                 verbose_name='кол-во',
                                 help_text='Введите количество',
                                 blank=True
                                 )

    def clean(self):
        part = self.part
        oil = self.oil
        service = self.service
        kit_service = self.kit_service

        related_fields = [part, oil, service, kit_service]
        related_fields_selected = [field for field in related_fields if field]
        if len(related_fields_selected) > 1:
            raise ValidationError('Выбирете, пожалуйста, только одну позицию - ЗЧ, Масло, Работу или Набор из работ')
        if (part and part.stock == 0) or (oil and oil.stock == 0):
            raise ValidationError('На складе больше нет таких ЗЧ/ масла')

    class Meta:
        verbose_name_plural = 'Позиции в ЗН'


@receiver(post_save, sender=WorkOrderItem, )
def check_warehouse(sender, instance, **kwargs):
    if instance.work_order.is_editable and instance.part and instance.part.is_available == True:
        if instance.part.stock > 0:
            instance.part.stock -= instance.amount
            instance.part.save()
    elif instance.work_order.is_editable and instance.oil and instance.oil.is_available == True:
        if instance.oil.stock > 0:
            instance.oil.stock -= instance.amount
            instance.oil.save()
