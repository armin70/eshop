from django.contrib import admin
from .models import ShopCart, Order, Purchase
# Register your models here.


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity',
                    'model', 'price', 'size', 'amount', 'qr']
    list_filter = ('uid',)


admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order)
admin.site.register(Purchase)
