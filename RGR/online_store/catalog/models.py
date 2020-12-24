from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)                                      #название категории
    slug = models.SlugField(max_length=200, unique=True)                                        #для формирования понятных человеку URL
    class Meta:                                                                                 #класс внутри модели содержит метаданные
        ordering = ('name',)                                                                    #порядок сортировки данных
        verbose_name = 'category'                                                               #метка поля для запроса (удобно читаемое имя поля)
        verbose_name_plural = 'categories'
    def __str__(self):                                                                          #возвращает отображение объекта, понятное человеку
        return self.name
    def get_absolute_url(self):                                                                 #get_absolute_url() для формирования URL для конкретного объекта
        return reverse('catalog:product_list_by_category', args=[self.slug])                    #получаем URL, указав имя шаблона и параметры

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)   #ForeignKey на модель Category, это отношение «многие к одному» – каждый товар принадлежит к одной категории, но каждая категория может включать множество товаров
    name = models.CharField(max_length=200, db_index=True)                                      #название товара
    slug = models.SlugField(max_length=200, db_index=True)                                      #уникальное поле слага, которое будем использовать для построения человекопонятных URL’ов
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)                        #изображение товара (не являющееся обязательным)
    description = models.TextField(blank=True)                                                  #описание товара (не являющееся обязательным)
    price = models.DecimalField(max_digits=10, decimal_places=2)                                #DecimalField - чтобы избежать проблем с округлением цен
    available = models.BooleanField(default=True)                                               #наличиe товара
    created = models.DateTimeField(auto_now_add=True)                                           #дата и время создания товара
    updated = models.DateTimeField(auto_now=True)                                               #дата и время последнего изменения
    class Meta:                                                                                 #класс внутри модели содержит метаданные
        ordering = ('name',)                                                                    #сортировка
        index_together = (('id', 'slug'),)                                                      #индекс по двум полям, id и slug, в дальнейшем мы будем запрашивать товары по их id и слагу - ускорит выборку объектов
    def __str__(self):                                                                          #возвращает отображение объекта, понятное человеку
        return self.name
    def get_absolute_url(self):                                                                 #get_absolute_url() для формирования URL для конкретного объекта
        return reverse('catalog:product_detail', args=[self.id, self.slug])                     #формирует URL объекта

