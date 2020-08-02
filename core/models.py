from django.conf import settings
from django.db import models
from django.shortcuts import reverse

# LABEL_CHOICES = (
#     ('lbl1', 'lbl_1'),
#     ('lbl2', 'lbl_2'),
#     ('lbl3', 'lbl_3'),
# )


class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


# choices = Category.objects.all().values_list('name', 'name')


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    img_url = models.ImageField(default="product")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, max_length=255, default=1)
    # label = models.CharField(choices=LABEL_CHOICES, max_length=5)

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


class ItemImages (models.Model):
    item = models.ForeignKey(
        Item, default=None, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.item.title


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
