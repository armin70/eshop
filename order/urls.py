from django.urls import path
from .views import order, addToCart, cart, updateCart, deleteOrder, checkout, getInfo, payment, purchase, idpay

app_name = 'order'

urlpatterns = [
    path('', order, name='order'),
    path('addtocart/<int:id>/', addToCart, name="add_to_cart"),
    path('cart', cart, name="cart"),
    path('checkout', checkout, name="checkout"),
    path('payment', payment, name="payment"),
    path('pay', idpay, name="pay"),
    path('purchase', purchase, name="purchase"),
    path('updateCart', updateCart, name="updateCart"),
    path('deleteOrder', deleteOrder, name="deleteOrder"),
    path('getinfo', getInfo, name="getInfo"),
]
