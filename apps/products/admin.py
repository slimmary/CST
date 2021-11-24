from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Part, OilContainer, Oil, Work, KitService


class PartAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('product_name',
                    'in_price',
                    'out_price',
                    'part_number_original',
                    'part_manufacturer',
                    'part_number_cross',
                    'part_provider',
                    'stock',
                    'is_available'
                    )
    list_filter = ('part_number_original',
                   'part_number_cross',
                   'part_provider',
                   'is_available'
                   )

    search_fields = ['part_number_original',
                     'part_number_cross',
                     'part_provider'
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


class WorkAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('service_name',
                    'work_our',

                    )
    list_filter = ('service_name',
                   'work_our',
                   )

    search_fields = ['service_name',
                     ]


class KitServiceAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('service_name',
                    'get_link_to_services',
                    'work_our',
                    )
    list_filter = ('service_name',
                   'work_our',
                   'services__service_name'
                   )

    search_fields = ['service_name',
                     ]

    def get_link_to_services(self, obj):
        return format_html(", ".join(["<a href={}> {} \n</a>".format(reverse(
            'admin:products_work_change', args=(work.pk,)), str(work)) for work in obj.services.all()]))

    get_link_to_services.short_description = 'Перечень работ'


admin.site.register(Part, PartAdmin)
admin.site.register(OilContainer, OilContainerAdmin)
admin.site.register(Oil, OilAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(KitService, KitServiceAdmin)
