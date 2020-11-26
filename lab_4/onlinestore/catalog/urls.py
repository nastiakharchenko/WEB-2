from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_list, name='product_list'),                                  #product_list вызовет функцию без дополнительных параметров
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'), #product_list_by_category вызовет функцию, передав в качестве аргумента слаг - category_slug
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),         #шаблон для отображения страницы подробностей товара. Он вызовет функцию product_detail с двумя дополнительными параметрами: id и slug.
]