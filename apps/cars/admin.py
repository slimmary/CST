from django.contrib import admin
from .models import Car, BrandModel


class BrandModelAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('brand',
                    'model',
                    )
    list_filter = (
        'brand',
    )

    search_fields = [
        'model',
    ]


class CarAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('brand_model',
                    # 'client',
                    'year_manufacturing',
                    'car_number',
                    'other_char',
                    )

    search_fields = [
        'brand_model',
        'car_number',
    ]


admin.site.register(Car, CarAdmin)
admin.site.register(BrandModel, BrandModelAdmin)