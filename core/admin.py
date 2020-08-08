from .models import Item, Category, ItemImages, ContactUs, Tag, ItemPrice
from django.contrib import admin


# admin.site.register(OrderItem)
# admin.site.register(Order)
admin.site.register(Category)
admin.site.register(ItemPrice)
admin.site.register(ContactUs)


class ItemImageAdmin(admin.StackedInline):
    model = ItemImages


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageAdmin]

    class meta:
        model = Item


# @admin.register(ItemImages)
# class ItemImageAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Tag)
