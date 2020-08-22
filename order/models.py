from django.db import models
from django.contrib.auth.models import User
from core.models import Product, ProductType
from django.forms import ModelForm


# Create your models here.


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.IntegerField(null=True)
    model = models.CharField(max_length=250, null=True)
    slug = models.SlugField(max_length=500, null=True)
    size = models.CharField(max_length=5, null=True)
    uid = models.IntegerField(null=True)
    amount = models.IntegerField(null=True)
    qr = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} عدد {self.product.title} رنگ {self.model}"

    # @property
    # def price(self):
    #     return self.model.price

    # @property
    # def amount(self):
    #     return(self.quantity * self.model.price)


class Order(models.Model):
    uid = models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(ShopCart)
    total = models.IntegerField(default=False)

    def __str__(self):
        return self.user.username


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity', 'model', 'price', 'size', 'uid', 'qr']


class UpdateCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity', 'slug']


class deleteCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['slug']
