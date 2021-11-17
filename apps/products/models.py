from django.core.validators import MinValueValidator
from django.db import models
from datetime import date
from django.db.models.signals import m2m_changed


class Products(models.Model):
    product_name = models.CharField(max_length=100,
                                    verbose_name='Название',
                                    help_text='Введите названия продукта/услуги',
                                    )
    in_price = models.PositiveIntegerField(default=0,
                                           verbose_name='Себестоимость грн.',
                                           help_text='Введите цену от поставщика продукта/услуги',
                                           )
    out_price = models.PositiveIntegerField(default=0,
                                            verbose_name='Стоимость грн.',
                                            help_text='Введите цену для клиента продукта/услуги',
                                            )

    class Meta:
        abstract = True


class Detail(Products):
    detail_number_original = models.CharField(max_length=100,
                                              verbose_name='№ детали оригинал',
                                              help_text='Введите № детали по каталогу оригинального производителя ',
                                              )
    detail_manufacturer = models.CharField(max_length=100,
                                           verbose_name='производитель детали',
                                           help_text='Введите название поставщика детали',
                                           )
    detail_number_cross = models.CharField(null=True,
                                           max_length=100,
                                           verbose_name='cross № детали',
                                           help_text='Введите № детали по "заменителю"',
                                           blank=True)
    detail_provider = models.CharField(max_length=100,
                                       verbose_name='поставщик детали',
                                       help_text='Введите название поставщика детали',
                                       )
    stock = models.PositiveIntegerField(default=1,
                                        verbose_name='кол-во',
                                        help_text='Введите количество деталей',
                                        )
    is_available = models.BooleanField(verbose_name='на склад',
                                       help_text='для добавления детали на склад поставьте галочку',
                                       default=False)

    def __str__(self):
        return '{} №{} {} cross№{} поставщик {}'.format(self.product_name,
                                                        self.detail_number_original,
                                                        self.detail_manufacturer,
                                                        self.detail_number_cross,
                                                        self.detail_provider)

    class Meta:
        verbose_name_plural = 'Детали'


class OilContainer(models.Model):
    container_date = models.DateField(default=date.today,
                                      verbose_name='Дата поступления на склад',
                                      help_text='Выберите дату')

    class ContainerL:
        one = '1л'
        two = '2л'
        five = '5л'
        ten = '10л'
        twenty = '20л'

    L_CHOICE = (
        (ContainerL.one, '1л'),
        (ContainerL.two, '2л'),
        (ContainerL.five, '5л'),
        (ContainerL.ten, '10л'),
        (ContainerL.twenty, '20л'),
    )

    volume = models.CharField(null=True,
                              max_length=100,
                              choices=L_CHOICE,
                              verbose_name='Объём тары',
                              help_text='Выберите объём тары'
                              )

    def __str__(self):
        return '{} {}'.format(self.container_date, self.volume)

    class Meta:
        verbose_name_plural = 'Фасовка масла'


class Oil(Products):
    stock_l = models.DecimalField(decimal_places=2,
                                  max_digits=12,
                                  default=1,
                                  verbose_name='кол-во',
                                  help_text='Введите количество л',
                                  validators=[MinValueValidator(0.00)]
                                  )
    is_available = models.BooleanField(verbose_name='на склад',
                                       help_text='для добавления масла на склад поставьте галочку',
                                       default=False
                                       )
    container = models.OneToOneField(OilContainer,
                                     on_delete=models.CASCADE,
                                     related_name='oil',
                                     verbose_name='Тара',
                                     help_text='Выберите тару, в которой поступило масло'
                                     )

    def __str__(self):
        return '{} объём масла {} '.format(self.product_name, self.stock_l)

    class Meta:
        verbose_name_plural = 'Масло'


class Service(Products):
    work_our = models.DecimalField(decimal_places=2,
                                   max_digits=12,
                                   default=1,
                                   verbose_name='нормо-часы',
                                   help_text='Введите количество часов',
                                   validators=[MinValueValidator(0.00)]
                                   )

    def __str__(self):
        return '{} {}ч'.format(self.product_name, self.work_our)

    class Meta:
        verbose_name_plural = 'Услуги (работы)'


class KitService(Products):
    services = models.ManyToManyField(Service,
                                      verbose_name='набор работ',
                                      help_text='Выберите работы из которых состоит услуга',
                                      )

    kit_work_ours = models.DecimalField(decimal_places=2,
                                        max_digits=12,
                                        default=0,
                                        verbose_name='нормо-часы',
                                        help_text='Поле заполнится автоматически',
                                        )


    # def save(self, *args, **kwargs):
    #     count_work_our = 0
    #     kit_in_price = 0
    #     kit_out_price = 0
    #     for work in self.services.all():
    #         count_work_our += work.work_our
    #         kit_in_price += work.in_price
    #         kit_out_price += work.out_price
    #     self.kit_work_ours = count_work_our
    #     self.in_price = kit_in_price
    #     self.out_price = kit_out_price
    #
    #     super().save(*args, **kwargs)


    def __str__(self):
        return '{} {}ч'.format(self.product_name, self.kit_work_ours)

    class Meta:
        verbose_name_plural = 'Услуги (набор работ)'


KitService._meta.get_field('in_price').help_text = 'Поле заполнится автоматически'
KitService._meta.get_field('out_price').help_text = 'Поле заполнится автоматически'


