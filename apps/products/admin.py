from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Detail, OilContainer, Oil, Service, KitService


class DetailAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('product_name',
                    'in_price',
                    'out_price',
                    'detail_number_original',
                    'detail_manufacturer',
                    'detail_number_cross',
                    'detail_provider',
                    'stock',
                    'is_available'
                    )
    list_filter = ('detail_number_original',
                   'detail_number_cross',
                   'detail_provider',
                   'is_available'
                   )

    search_fields = ['detail_number_original',
                     'detail_number_cross',
                     'detail_provider'
                     ]


class OilContainerAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('volume',)
    list_filter = ('volume',)


class OilAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('product_name',
                    'in_price',
                    'out_price',
                    'stock_l',
                    'is_available',
                    'get_container_date',
                    'get_container_volume',
                    )
    list_filter = ('product_name',
                   'container__volume',
                   'container__container_date',
                   'stock_l',
                   'is_available'
                   )

    search_fields = ['product_name',
                     'detail_number_cross',
                     'detail_provider'
                     ]

    def get_container_date(self, obj):
        return obj.container.container_date

    get_container_date.short_description = 'Дата поступления'

    def get_container_volume(self, obj):
        return obj.container.volume

    get_container_volume.short_description = 'Тара'


class ServiceAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('product_name',
                    'in_price',
                    'out_price',
                    'work_our',

                    )
    list_filter = ('product_name',
                   'work_our',
                   )

    search_fields = ['product_name',
                     ]


class KitServiceAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('product_name',
                    'in_price',
                    'out_price',
                    'kit_work_ours',
                    'get_link_to_services',
                    )
    list_filter = ('product_name',
                   'kit_work_ours',
                   'services__product_name'
                   )

    search_fields = ['product_name',
                     ]

    def get_link_to_services(self,obj):
        return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
            'admin:products_service_change', args=(service.pk,)), str(service)) for service in obj.services.all()]))

    get_link_to_services.short_description = 'Перечень работ'


admin.site.register(Detail, DetailAdmin)
admin.site.register(OilContainer, OilContainerAdmin)
admin.site.register(Oil, OilAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(KitService, KitServiceAdmin)
