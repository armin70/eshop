from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Item, Order, OrderItem


def index(req):
    context = {
        'items': Item.objects.all()
    }
    return render(req, "index.html", context)


class ProductsView(ListView):
    model = Item
    template_name = "products.html"


class ProductDetailsView(DetailView):
    model = Item
    template_name = "products_details.html"


def cart(req):

    return render(req, "cart.html")


def add_to_cart(req, id):
    item = get_object_or_404(Item, id=id)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=req.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=req.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(req, "this item updated")
        else:
            messages.info(req, "this item added")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=req.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(req, "this item added")
    return redirect("core:products_details", pk=id)


def remove_from_cart(req, id):
    item = get_object_or_404(Item, id=id)
    order_qs = Order.objects.filter(user=req.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=req.user,
                ordered=False
            )[0]
            order.items.remove(id)
            messages.info(req, "this item removed")
            return redirect("core:products_details", pk=id)
        else:
            messages.info(req, "this item was not in your cart")
            return redirect("core:products_details", pk=id)

    else:
        messages.info(req, "you do not have an order")
        return redirect("core:products_details", pk=id)
