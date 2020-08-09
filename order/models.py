from django.db import models
from django.contrib.auth.models import User
from core.models import Product, ProductType
from django.forms import ModelForm

# Create your models here.


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.CharField(max_length=250, null=True)
    model = models.CharField(max_length=250, null=True)
    slug = models.SlugField(max_length=500, null=True)
    size = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.product.title

    # @property
    # def price(self):
    #     return self.model.price

    # @property
    # def amount(self):
    #     return(self.quantity * self.model.price)


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity', 'model', 'price', 'size']
