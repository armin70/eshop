from django.db import models
from django.contrib.auth.models import User
from core.models import Product, ProductType
from django.forms import ModelForm, TextInput, Textarea


# Create your models here.


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default=False)
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
    ordered = models.BooleanField(default=False)
    name = models.CharField(max_length=2000, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    zip_code = models.CharField(max_length=25, null=True, blank=True)
    tel = models.CharField(max_length=11, null=True, blank=True)
    cart_total = models.IntegerField(null=True, blank=True)
    orderId = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class CheckOutForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'address', 'zip_code', 'tel', 'cart_total']


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


class Purchase(models.Model):
    product = models.CharField(max_length=4000, verbose_name="نوع محصول")
    name = models.CharField(max_length=500, verbose_name="نام گیرنده")
    zip_code = models.CharField(max_length=500, verbose_name="کد پستی")
    tel = models.CharField(max_length=17, verbose_name="موبایل")
    address = models.TextField(verbose_name="آدرس")
    familiar = models.CharField(
        max_length=2000, blank=True, null=True, verbose_name="نحوه آشنایی")
    criticism = models.CharField(
        max_length=2000, blank=True, null=True, verbose_name="انتقاد")

    def __str__(self):
        return self.name


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ['name', 'product', 'zip_code',
                  'tel', 'address', 'familiar', 'criticism']
        widgets = {
            'product': TextInput(attrs={'placeholder': 'نام محصول'}),
            'name': TextInput(attrs={'placeholder': 'نام و نام خانوادگی'}),
            'zip_code': TextInput(attrs={'placeholder': 'کد پستی'}),
            'tel': TextInput(attrs={'placeholder': 'شماره موبایل'}),
            'address': Textarea(attrs={'placeholder': 'آدرس'}),
            'familiar': TextInput(attrs={'placeholder': 'نحوه آشنایی'}),
            'criticism': TextInput(attrs={'placeholder': 'انتقاد'})
        }
