from django.contrib import admin
from .models import ClientProfile


class ClientProfileAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ('name',
                    'phone',
                    'user'
                    )
    list_display_links = ('name',
                          'phone',
                          )
    list_filter = ('phone',
                   'name',
                   )


admin.site.register(ClientProfile, ClientProfileAdmin)
