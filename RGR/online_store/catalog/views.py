from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm

#Страница списка товаров и их фильтрация:
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)                   #фильтрация товаров (сначала те, которые есть в наличие)
    if category_slug:                                                   #если задан category_slug (не обязательно) - фильтруем по нему
        category = get_object_or_404(Category, slug=category_slug)      #функция возвращает объект, который подходит по указанным параметрам, или вызывает исключение объект не найден
        products = products.filter(category=category)                   #фильтрация товаров (по категориям)
    return render(request, 'catalog/product/list.html',
              {'category': category,
               'categories': categories,
               'products': products})                                   #получаем URL, указав имя шаблона и параметры

#Отображение страницы каждого товара с его детальным описанием:
def product_detail(request, id, slug):                                  #id и slug для однозначного определения нужного товара
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()                            #получаем информацию о количестве единиц (после выбора)
    return render(request, 'catalog/product/detail.html', {'product': product, 'cart_product_form': cart_product_form})