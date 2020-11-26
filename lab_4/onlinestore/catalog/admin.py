from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']                                                 #такие параметры товара будут видны на странице с категориями
    prepopulated_fields = {'slug': ('name',)}                                       #настраиваем поле slug так, чтобы его значение формировалось автоматически из поля name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']     #такие параметры товара будут видны на странице
    list_filter = ['available', 'created', 'updated']                               #фильтрация данных
    list_editable = ['price', 'available']                                          #возможность изменять перечисленные поля со страницы списка товаров, не переходя к форме редактирования товара
    prepopulated_fields = {'slug': ('name',)}                                       #настраиваем поле slug так, чтобы его значение формировалось автоматически из поля name
