from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ShopCart, ShopCartForm, UpdateCartForm, Order, deleteCartForm
# Create your views here.


def checkout(request):
    return render(request, "checkout.html")


def cart(request):
    cart = ShopCart.objects.filter(uid=request.session['uid'])
    return render(request, "cart.html", {'cart': cart})


def order(request):
    return render(request, "order.html")


# @login_required(login_url='/login')
def addToCart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkproduct = ShopCart.objects.filter(
        slug=f"{request.POST['model']}_{request.POST['size']}_{id}_{request.POST['uid']}_{request.POST.get('qr',False)}_{request.POST['price']}")
    print(
        f"{request.POST['model']}_{request.POST['size']}_{id}_{request.POST['uid']}_{request.POST.get('qr',False)}_{request.POST['price']}")
    if checkproduct:
        control = 1
    else:
        control = 0
    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(
                    slug=f"{request.POST['model']}_{request.POST['size']}_{id}_{request.POST['uid']}_{request.POST.get('qr',False)}_{request.POST['price']}")
                data.quantity += form.cleaned_data['quantity']
                data.model = form.cleaned_data['model']
                data.price = form.cleaned_data['price']
                data.size = form.cleaned_data['size']
                data.uid = form.cleaned_data['uid']
                data.qr = form.cleaned_data['qr']
                data.amount = form.cleaned_data['price'] * data.quantity
                data.save()
                print(
                    f"{request.POST['model']}_{request.POST['size']}_{id}_{request.POST['uid']}_{request.POST.get('qr',False)}_{request.POST['price']}")
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.model = form.cleaned_data['model']
                data.price = form.cleaned_data['price']
                data.size = form.cleaned_data['size']
                data.uid = form.cleaned_data['uid']
                data.qr = form.cleaned_data['qr']
                data.slug = f"{request.POST['model']}_{request.POST['size']}_{id}_{request.POST['uid']}_{request.POST.get('qr',False)}_{request.POST['price']}"
                data.amount = form.cleaned_data['price'] * data.quantity
                request.session['uid'] = form.cleaned_data['uid']
                data.save()
                order_qs = Order.objects.filter(uid=request.session['uid'])
                if order_qs:
                    order = order_qs[0]
                    order.user_id = current_user.id
                    order.uid = form.cleaned_data['uid']
                    order.save()
                    order.items.set(ShopCart.objects.filter(
                        uid=request.session['uid']))
                else:
                    newOrder = Order()
                    newOrder.user_id = current_user.id
                    newOrder.uid = form.cleaned_data['uid']
                    newOrder.save()
                    newOrder.items.set(ShopCart.objects.filter(
                        uid=request.session['uid']))

        messages.success(request, 'محصول به سبد خرید اضافه شد')
        return HttpResponseRedirect(url)
    else:
        messages.warning(request, 'محصول به سبد خرید اضافه نشد')


def updateCart(request):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkproduct = ShopCart.objects.filter(slug=request.POST['slug'])
    print(request.POST['slug'])
    if checkproduct:
        control = 1
    else:
        control = 0
    if request.method == 'POST':
        form = UpdateCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(slug=request.POST['slug'])
                print(data)
                data.quantity = form.cleaned_data['quantity']
                data.amount = form.cleaned_data['quantity'] * data.price
                data.save()
                messages.success(request, 'محصول به روز رسانی شد')
            else:
                messages.warning(request, 'محصول وجود ندارد')
                return HttpResponseRedirect(url)

        return HttpResponseRedirect(url)
    else:
        messages.warning(request, 'محصول به سبد خرید اضافه نشد')


def deleteOrder(request):
    url = request.META.get('HTTP_REFERER')
    if 'slug' in request.POST:
        slug = request.POST['slug']
    else:
        slug = 'False'
    checkproduct = ShopCart.objects.filter(slug=slug)
    if checkproduct:
        control = 1
    else:
        control = 0
    if request.method == 'POST':
        form = deleteCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.filter(slug=slug)
                data.delete()
            else:
                return HttpResponseRedirect(url)
            return HttpResponseRedirect(url)
    else:
        messages.warning(request, 'محصول حذف نشد')
        return HttpResponseRedirect(url)
