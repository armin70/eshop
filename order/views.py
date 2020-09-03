from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import requests
import json
import time

from .models import ShopCart, ShopCartForm, UpdateCartForm, Order, deleteCartForm, Order, CheckOutForm, PurchaseForm
# Create your views here.


def checkout(request):
    order = Order.objects.filter(uid=request.session['uid'], ordered=False)
    cart = ShopCart.objects.filter(uid=request.session['uid'], ordered=False)
    return render(request, "checkout.html", {'order': order[0], 'cart': cart})


def payment(request):
    order = Order.objects.filter(uid=request.session['uid'], ordered=False)
    return render(request, "payment.html", {'order': order[0]})


def cart(request):
    cart = ShopCart.objects.filter(uid=request.session['uid'], ordered=False)
    print(cart)
    if cart:
        return render(request, "cart.html", {'cart': cart})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@csrf_exempt
def callback(request):
    mydict = dict(request.POST)
    context = {
        'id': mydict['id'][0],
        'order_id': mydict['order_id'][0],
    }
    print(context['id'][0])
    return render(request, 'callback.html', context)


def purchase(req):
    form = PurchaseForm(req.POST, None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(req, "purchase.html", context)


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


def getInfo(request):
    url = request.META.get('HTTP_REFERER')
    checkproduct = Order.objects.filter(uid=request.session['uid'])
    if checkproduct:
        control = 1
    else:
        control = 0
    if request.method == 'POST':
        form = CheckOutForm(request.POST)
        if form.is_valid():
            if control == 1:
                order = Order.objects.get(id=request.POST['id'])
                order.name = form.cleaned_data['name']
                order.address = form.cleaned_data['address']
                order.zip_code = form.cleaned_data['zip_code']
                order.tel = form.cleaned_data['tel']
                order.cart_total = form.cleaned_data['cart_total']
                order.save()
                url = 'https://api.idpay.ir/v1.1/payment'
                body = {
                    'order_id': request.POST['id'],
                    'amount': 10000,
                    'name': form.cleaned_data['name'],
                    'phone': form.cleaned_data['tel'],
                    'callback': 'https://abadis-shop.ir/order/callback',
                }
                headers = {
                    'Content-Type': 'application/json',
                    'X-API-KEY': 'db6d4b4b-5564-4917-b512-02e6aab6aebb',
                }
                r = requests.post(url, data=json.dumps(body), headers=headers)
                json_content = json.loads(r.text)
                if r.status_code == 201:
                    order.orderId = json_content['id']
                    return HttpResponseRedirect(json_content['link'])
                else:
                    return HttpResponse(json_content["error_message"])
        else:
            return HttpResponseRedirect(url)

    else:
        return HttpResponseRedirect(url)


def verify(request):
    if request.method == 'POST':
        url = 'https://api.idpay.ir/v1.1/payment/verify'
        body = {
            'id': request.POST['id'],
            'order_id': request.POST['order_id'],
        }
        headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': 'db6d4b4b-5564-4917-b512-02e6aab6aebb',
        }
        r = requests.post(url, data=json.dumps(body), headers=headers)
        json_content = json.loads(r.text)
        print(json_content)
        if r.status_code == 200:
            return HttpResponse('success')
        else:
            return HttpResponse('failed')
