from django.urls import path
from . import views

urlpatterns = [
    path('', views.product, name='product'),
    path('api/get_products/', views.get_product, name='get_product'),
]