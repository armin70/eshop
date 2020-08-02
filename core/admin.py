from django.contrib import admin

from .models import Item, OrderItem, Order, Category, ItemImages

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Category)


class ItemImageAdmin(admin.StackedInline):
    model = ItemImages


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageAdmin]

    class meta:
        model = Item


@admin.register(ItemImages)
class ItemImageAdmin(admin.ModelAdmin):
    pass
