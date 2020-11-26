from decimal import Decimal
from django.conf import settings
from catalog.models import Product

class Cart(object):
    def __init__(self, request):
        #Инициализация объекта корзины
        self.session = request.session                                                   #запоминаем текущую сессию
        cart = self.session.get(settings.CART_SESSION_ID)                                #пытаемся получить данные корзины
        if not cart:                                                                     #если данных нет -
            cart = self.session[settings.CART_SESSION_ID] = {}                           #сохраняем в сессии пустую корзину
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        #product, который нужно добавить или обновить
        #quantity - не являющееся обязательным количество объектов, по умолчанию 1
        #update_quantity - булевое значение, которое говорит о том, нужно ли заменить значение количества товаров на новое (True) или следует добавить его к существующему (False)

        #Добавление товара в корзину или обновление его количества:
        product_id = str(product.id)
        if product_id not in self.cart:                                                   #если товара нет в корзине
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:                                                               #если количество товара нужно обновить:
            self.cart[product_id]['quantity'] = quantity
        else:                                                                             #иначе
            self.cart[product_id]['quantity'] += quantity                                 #добавляем количество единиц
        self.save()

    def save(self):
        self.session.modified = True                                                      #помечаем сессию как измененную

    #Метод remove() удаляет товар из корзины и сохраняет новые данные сессии, обращаясь к методу save():
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    #Метод проходит по товарам корзины и получает соответствующие объекты Product:
    def __iter__(self):
        """
        Создаем копию объекта корзины, получаем товары, сохраненные в ней.
        Для каждого товара преобразуем цену из строки в число с фиксированной точностью,
        вычисляем общую стоимость, total_price, с учетом цены и количества.
        """
        if self.cart:
            product_ids = self.cart.keys()
            products = Product.objects.filter(id__in=product_ids)
            cart = self.cart.copy()
            for product in products:
                cart[str(product.id)]['product'] = product
            for item in cart.values():
                item['price'] = Decimal(item['price'])
                item['total_price'] = item['price'] * item['quantity']
            yield item

    #Метод возвращает общее количество товаров в корзине:
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    #Метод для подсчета общей стоимости корзины:
    def get_total_price(self):
        return sum(
            Decimal(item['price']) * item['quantity']
            for item in self.cart.values()
        )

    #Метод очистки корзины:
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()