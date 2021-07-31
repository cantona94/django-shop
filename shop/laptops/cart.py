from django.conf import settings
from .models import Product


class Cart(object):

    def __init__(self, request):

        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавление в корзину
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'name': product.name,
                                     'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

        product.availabilityToCart += 1
        product.save()

    def plus_quantity(self, product):
        """
        Увеличение количества продукта
        """

        product_id = str(product.id)
        self.cart[product_id]['quantity'] += 1
        self.save()

        product.availabilityToCart += 1
        product.save()

    def minus_quantity(self, product):
        """
        Уменьшение количества продукта
        """
        product_id = str(product.id)
        self.cart[product_id]['quantity'] -= 1
        self.save()

        product.availabilityToCart -= 1
        product.save()

    def save(self):
        # Обновление сессии
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            product.availabilityToCart = 0
            product.save()

    def get_total_quantity(self, product):
        """
        Количество товара в корзине
        """

        product_id = str(product.id)
        if product_id in self.cart:
            return self.cart[product_id]['quantity']

    def get_total_price_product(self, product):
        """
        Общее стоимость определенного товара в корзине
        """

        product_id = str(product.id)
        return int(self.cart[product_id]['price']) * int(self.cart[product_id]['quantity'])

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_len(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return sum(int(item['price']) * item['quantity'] for item in
            self.cart.values())

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_cart(self):
        return self.cart