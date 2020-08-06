from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Item, Order, OrderItem, Category, ItemImages
from .forms import ContactUsForm


def index(req):
    context = {
        'items': Item.objects.all()[:10],
    }
    return render(req, "index.html", context)


def contactUs(req):
    form = ContactUsForm(req.POST, None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(req, "contact.html", context)


def about(req):
    return render(req, "about.html")


class ProductsView(ListView):
    model = Item
    ordering = "-timestamp"
    paginate_by = 16
    template_name = "products.html"


# class ProductDetailsView(DetailView):
#     model = Item

#     def get_queryset(self, **kwargs):
#         context = super(ProductDetailsView, self).get_context_data(**kwargs)
#         context['iamges'] = Item.objects.filter(pk=self.kwargs.get('pk'))
#         return context
#     template_name = "products_details.html"


def ProductDetails(req, pk):
    item = get_object_or_404(Item, id=pk)
    photos = ItemImages.objects.filter(item=item)
    return render(req, 'products_details.html', {"item": item, "photos": photos})


def CategoryView(req, id):
    category = Category.objects.filter(id=id)
    category_items_list = Item.objects.filter(
        category=category[0]).order_by("-timestamp")
    paginator = Paginator(category_items_list, 12)
    page_number = req.GET.get('page')
    category_items = paginator.get_page(page_number)
    return render(req, 'category.html', {"category": category[0], "category_items": category_items, "page_number": page_number})


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
