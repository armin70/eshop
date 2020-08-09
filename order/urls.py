from django.urls import path
from .views import order, addToCart

app_name = 'order'

urlpatterns = [
    path('', order, name='order'),
    path('addtocart/<int:id>/', addToCart, name="add_to_cart"),
]
