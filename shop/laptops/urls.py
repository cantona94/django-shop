from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('api/get_products/', views.get_product, name='get_product'),
    path('cart/', views.cart, name='cart'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]