from .models import Product, Category, ProductImages, ContactUs, Tag, ProductType
from django.contrib import admin


# admin.site.register(OrderItem)
# admin.site.register(Order)
admin.site.register(Category)
admin.site.register(ProductType)
admin.site.register(ContactUs)


class ProductImageAdmin(admin.StackedInline):
    model = ProductImages


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    class meta:
        model = Product


# @admin.register(ItemImages)
# class ItemImageAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Tag)
