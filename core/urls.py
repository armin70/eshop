from django.urls import path
from .views import index, ProductsView, ProductDetails, add_to_cart, remove_from_cart, CategoryView, contactUs, about

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('add-to-cart/<int:id>/', add_to_cart, name="add_to_cart"),
    path('remove-from-cart/<int:id>/', remove_from_cart, name="remove_from_cart"),
    path('products', ProductsView.as_view(), name="products"),
    path('contact', contactUs, name="contactUs"),
    path('about', about, name="aboutUs"),
    path('products/<int:pk>/', ProductDetails, name="products_details"),
    path('categories/<int:id>/', CategoryView)
]
