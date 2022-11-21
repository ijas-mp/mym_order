from django.contrib import admin
from core import models


class AddressAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Address, AddressAdmin)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Order, OrderAdmin)
