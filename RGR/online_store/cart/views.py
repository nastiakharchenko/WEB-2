from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from catalog.models import Product
from .cart import Cart
from .forms import CartAddProductForm

@require_POST                                                       #чтобы обратиться к функции можно было только методом POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)                         #для работы с корзиной создаем форму
    if form.is_valid():                                             #и если она валидна -
        cd = form.cleaned_data                                      #обновляем и добавляем сведения о товаре
        cart.add(product=product,
                quantity=cd['quantity'],
                update_quantity=cd['update'])
    return redirect('cart:cart_detail')                             #перенаправляем пользователя на URL, где он увидит содержимое своей корзины

def cart_remove(request, product_id):
    """
    Метод получает ID товара, вызывает его из базы данных и удаляет из корзины,
    после чего пользователь перенаправляется на страницу корзины
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)              #функция возвращает объект, который подходит по указанным параметрам, или вызывает исключение объект не найден
    cart.remove(product)                                             #удаляет товар из корзины
    return redirect('cart:cart_detail')

def cart_detail(request):
    '''
    Oбработчик для страницы списка товаров, добавленных в корзину
    '''
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})

