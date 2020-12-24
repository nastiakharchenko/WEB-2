from django.test import TestCase

from ..models import Order

class OrderModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        """Настроить неизмененные объекты, используемые всеми методами тестирования"""
        Order.objects.create(first_name='first name', last_name='last name', email='e@email.com', address='address', postal_code='08007', city='city')

    def test_first_name_label(self):
        order=Order.objects.get(id=1)                                               # Получение объекта для тестирования
        field_label = order._meta.get_field('first_name').verbose_name              # Получение метаданных поля для получения необходимых значений
        self.assertEquals(field_label,'first name')                                 # Сравнить значение с ожидаемым результатом. В случае провала теста, в выводе будет указано какое именно значение содержит метка

    def test_address_label(self):
        order=Order.objects.get(id=1)
        field_label = order._meta.get_field('address').verbose_name
        self.assertEquals(field_label, 'address')

    def test_last_name_max_length(self):
        order=Order.objects.get(id=1)
        max_length = order._meta.get_field('last_name').max_length
        self.assertEquals(max_length, 50)