from django.test import TestCase
from ..forms import OrderCreateForm

class OrderFormTest(TestCase):

    #проверка на создание экземпляра формы класса OrderCreateForm:
    def test_model_field_form(self):
        form_data = {'first_name': 'first name', 'last_name': 'last name', 'email': 'e@email.com', 'address': 'address', 'postal_code': '08007', 'city': 'city'}
        form = OrderCreateForm(data=form_data)
        self.assertTrue(form.is_valid())