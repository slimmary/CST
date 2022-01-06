from django.contrib import admin
from django.utils.html import format_html

from .models import WorkOrder, WorkOrderItem


class WorkOrderItemInline(admin.StackedInline):
    list_per_page = 20
    model = WorkOrderItem
    fields = ('part', 'oil', 'service', 'kit_service')


class WorkOrderAdmin(admin.ModelAdmin):
    list_per_page = 20
    inlines = [WorkOrderItemInline,]
    list_display = ('open_date',
                    'close_date',
                    'status',
                    'total_price',
                    'is_paid',
                    'get_car_link',
                    'av_price',
                    'total_in_price_parts',
                    'total_out_price_parts',
                    'total_price_services',
                    'comment'
                    )
    list_filter = ('open_date',
                   'close_date',
                   'status',
                   'is_paid',
                   'car',
                   )

    search_fields = ['car__car_number',
                     'car__vin',
                     'car__brand_model'
                     ]

    def get_car_link(self, obj):
        return format_html(
            "<a href='../../cars/car/%s/change/' >%s</a>" % (str(obj.car.id), str(obj.car)))

    get_car_link.short_description = 'Автомобиль'


class WorkOrderItemAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('work_order_link',
                    'part',
                    'oil',
                    'service',
                    'kit_service'
                    )

    search_fields = ['work_order__car__car_number',
                     'work_order__car__vin',
                     'work_order__car__brand_model__brand',
                     'work_order__car__brand_model__model',
                     'part__part_number_original',
                     'part__part_number_cross',
                     'part__part_provider',
                     'service__service_name',
                     'kit_service__service_name',
                     ]

    def work_order_link(self, obj):
        return format_html(
            "<a href='../../workorders/workorder/%s/change/' >%s</a>" % (str(obj.work_order.id), str(obj.work_order)))

    work_order_link.short_description = 'ЗН'


admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(WorkOrderItem, WorkOrderItemAdmin)
