from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import ShopCart, ShopCartForm
# Create your views here.


def order(request):
    return render(request, "order.html")


@login_required(login_url='/login')
def addToCart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checkproduct = ShopCart.objects.filter(
        slug=f"{request.POST['model']}_{request.POST['size']}_{id}")
    print(f"{request.POST['model']}_{request.POST['size']}_{id}")
    if checkproduct:
        control = 1
    else:
        control = 0
    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = ShopCart.objects.get(
                    slug=f"{request.POST['model']}_{request.POST['size']}_{id}")
                data.quantity += form.cleaned_data['quantity']
                data.model = form.cleaned_data['model']
                data.price = form.cleaned_data['price']
                data.size = form.cleaned_data['size']
                data.save()
                print(f"{request.POST['model']}_{request.POST['size']}_{id}")
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.model = form.cleaned_data['model']
                data.price = form.cleaned_data['price']
                data.size = form.cleaned_data['size']
                data.slug = f"{request.POST['model']}_{request.POST['size']}_{id}"
                data.save()
        messages.success(request, 'محصول به سبد خرید اضافه شد')
        return HttpResponseRedirect(url)
    else:
        messages.warning(request, 'محصول به سبد خرید اضافه نشد')
