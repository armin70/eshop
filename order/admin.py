from django.contrib import admin
from .models import ShopCart
# Register your models here.


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'model', 'price', 'size']


admin.site.register(ShopCart, ShopCartAdmin)
