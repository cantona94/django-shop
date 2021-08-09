from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('api/get_products/', views.get_product, name='get_product'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/quantity_plus/', views.quantity_plus, name='quantity_plus'),
    path('cart/quantity_minus/', views.quantity_minus, name='quantity_minus'),
    path('cart/clear_cart/', views.clear_cart, name='clear_cart'),
    path('cart/remove_cart_item/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/add_order/', views.add_order, name='add_order'),

]