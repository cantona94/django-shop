
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Product


from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


def cookie_city(request):
    city = '!'
    if request.method == 'GET':
        if 'city' in request.COOKIES:
            city = request.COOKIES['city']
    elif request.method == 'POST':
        city = request.POST.get('city')

    return city

@csrf_exempt
def product(request):
    all_products = Product.objects.all()

    city = cookie_city(request)

    response = render(request, 'base.html', {
        'all_products': all_products, 'city': city,
    })

    response.set_cookie('city', city)
    return response


@api_view(['GET'])
def get_product(request):
    name = request.query_params.get('name', None)
    product_cag = request.query_params.get('product_cag', None)
    sort_product = request.query_params.get('sort_product', None)

    product = Product.objects.all()
    if name:
        product = product.filter(name__icontains=name)
    if product_cag:
        product = product.filter(category=product_cag)
    if sort_product:
        if sort_product == 'rating':
            product = product.all().order_by('-rating')
        elif sort_product == 'price':
            product = product.all().order_by('-price')
        elif sort_product == 'name':
            product = product.all().order_by('name')
    if product:
        serialized = ProductSerializer(product, many=True)
        return Response(serialized.data)
    else:
        return Response({})
