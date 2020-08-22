from django.conf import settings
from django.db import models
from django.shortcuts import reverse
from django.dispatch import receiver

model_choice = [
    ('single', 'single'),
    ('set', 'set'),
    ('family', 'family'),
]


class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(default="category")
    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


@receiver(models.signals.post_delete, sender=Category)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


class Tag(models.Model):
    name = models.CharField(max_length=250)
    @staticmethod
    def get_all_tags():
        return Tag.objects.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

# choices = Category.objects.all().values_list('name', 'name')


class ProductType(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    small = models.BooleanField(default=True)
    @staticmethod
    def get_all_tags():
        return ProductType.objects.all()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    model = models.ManyToManyField(ProductType, default="white")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    img_url = models.ImageField(default="product")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, max_length=255, default=1)
    label = models.ManyToManyField(Tag, blank=True)
    count = models.CharField(choices=model_choice,
                             default="single", max_length=200)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:products_details", kwargs={
            "pk": self.id
        })

    def get_add_to_cart_url(self):
        return reverse("core:add_to_cart", kwargs={
            "id": self.id
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove_from_cart", kwargs={
            "id": self.id
        })

    @property
    def get_price(self):
        price = []
        for p in self.model.all():
            price.append(p.price)
        return min(price)
# @receiver(models.signals.post_delete, sender=Product)
# def submission_delete(sender, instance, **kwargs):
#     instance.img_url.delete(False)


class ProductImages (models.Model):
    product = models.ForeignKey(
        Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.product.title


@receiver(models.signals.post_delete, sender=ProductImages)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
    instance.product.img_url.delete(False)

# class OrderItem(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     ordered = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.quantity} of {self.item.title}"


# class Order(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                              on_delete=models.CASCADE)
#     items = models.ManyToManyField(OrderItem)
#     start_date = models.DateTimeField(auto_now_add=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username


class ContactUs(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    tel = models.CharField(max_length=17, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField()
