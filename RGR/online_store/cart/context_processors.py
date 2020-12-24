from .cart import Cart

def cart(request):
    """
    Инициируем корзину, передавая в конструктор объект текущего запроса,
    и добавляем в контекст в виде переменной cart
    """
    return {'cart': Cart(request)}