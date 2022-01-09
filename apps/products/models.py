from django.core.validators import MinValueValidator
from django.db import models
from datetime import date


class Products(models.Model):
    product_name = models.CharField(max_length=100,
                                    verbose_name='Название',
                                    help_text='Введите названия продукта',
                                    )
    in_price = models.PositiveIntegerField(default=0,
                                           verbose_name='Себестоимость грн.',
                                           help_text='Введите цену от поставщика продукта',
                                           )
    extra_charge = models.PositiveIntegerField(default=25,
                                               verbose_name='Наценка %',
                                               help_text='Введите сколько % необходимо добавить к себестоимости '
                                                         'продукта',
                                               )
    out_price = models.PositiveIntegerField(default=0,
                                            verbose_name='Стоимость грн.',
                                            help_text='Поле зааполнится автоматически',
                                            )
    is_available = models.BooleanField(verbose_name='на склад',
                                       help_text='для добавления на склад поставьте галочку',
                                       default=False
                                       )

    def save(self, *args, **kwargs):
        self.out_price = self.in_price + (self.in_price / 100 * self.extra_charge)

        super(Products, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class Service(models.Model):
    service_name = models.CharField(null=True,
                                    max_length=100,
                                    verbose_name='Название',
                                    help_text='Введите названия работы',
                                    )
    work_our = models.PositiveIntegerField(
        default=1,
        verbose_name='н.часы (AV)',
        help_text='Введите количество н.часов (AV, 1 = 5мин)',
    )

    class Meta:
        abstract = True


class Work(Service):

    def __str__(self):
        return '{} {}ч'.format(self.service_name, self.work_our)

    class Meta:
        verbose_name_plural = 'Услуги (работы)'


class KitService(Service):
    services = models.ManyToManyField(Work,
                                      related_name='kit_service',
                                      verbose_name='набор работ',
                                      help_text='Выберите работы из которых состоит услуга',
                                      )

    def __str__(self):
        return '{} {}ч'.format(self.service_name, self.work_our)

    class Meta:
        verbose_name_plural = 'Услуги (набор работ)'


class Part(Products):
    part_number_original = models.CharField(max_length=100,
                                            verbose_name='№ детали оригинал',
                                            help_text='Введите № детали по каталогу оригинального производителя ',
                                            )
    part_manufacturer = models.CharField(max_length=100,
                                         verbose_name='производитель детали',
                                         help_text='Введите название поставщика детали',
                                         )
    part_number_cross = models.CharField(null=True,
                                         max_length=100,
                                         verbose_name='cross № детали',
                                         help_text='Введите № детали по "заменителю"',
                                         blank=True)
    part_provider = models.CharField(max_length=100,
                                     verbose_name='поставщик детали',
                                     help_text='Введите название поставщика детали',
                                     )
    stock = models.PositiveIntegerField(default=1,
                                        verbose_name='кол-во',
                                        help_text='Введите количество деталей',
                                        )

    def __str__(self):
        return '{} №{} {} cross№{} поставщик {}'.format(self.product_name,
                                                        self.part_number_original,
                                                        self.part_manufacturer,
                                                        self.part_number_cross,
                                                        self.part_provider)

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

    container = models.ForeignKey(OilContainer,
                                  on_delete=models.CASCADE,
                                  related_name='oil',
                                  verbose_name='Тара',
                                  help_text='Выберите тару, в которой поступило масло'
                                  )
    # to do: auto-add default stock_l=container
    # @property
    # def default_stock(self):
    #     if self.container == self.container.ContainerL.two:
    #         self.stock_l = 2
    #     elif self.container == self.container.ContainerL.five:
    #         self.stock_l = 5
    #     elif self.container == self.container.ContainerL.ten:
    #         self.stock_l = 10
    #     elif self.container == self.container.ContainerL.twenty:
    #         self.stock_l = 20
    #     else:
    #         self.stock_l = 2
    #     return self.stock_l

    def __str__(self):
        return '{} объём масла {} '.format(self.product_name, self.stock_l)

    class Meta:
        verbose_name_plural = 'Масла'
