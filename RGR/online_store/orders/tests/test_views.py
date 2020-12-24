from django.test import TestCase, Client

class ViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_loads_properly(self):
        response = self.client.get('http://localhost:8000/orders/create/')
        self.assertEqual(response.status_code, 200)

    def test_post_response(self):
        response = self.client.post('http://localhost:8000/orders/create/')
        self.assertEqual(response.status_code, 200)