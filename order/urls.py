from django.urls import path
from .views import order, addToCart, checkout, updateCart, deleteOrder

app_name = 'order'

urlpatterns = [
    path('', order, name='order'),
    path('addtocart/<int:id>/', addToCart, name="add_to_cart"),
    path('cart', checkout, name="checkout"),
    path('updateCart', updateCart, name="updateCart"),
    path('deleteOrder', deleteOrder, name="deleteOrder"),
]
