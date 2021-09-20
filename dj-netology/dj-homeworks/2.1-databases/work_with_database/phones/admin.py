from django.contrib import admin
from phones.models import Phone


class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'release_date', 'lte_exists')


admin.site.register(Phone, PhoneAdmin)
