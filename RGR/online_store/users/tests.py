from django.test import TestCase, Client

class UsersViewsTestCase(TestCase):

    def setUp(self):
        self.client = Client()

    def test_post_response(self):
        response = self.client.post('http://localhost:8000/accounts/login/', {'username': 'fred', 'password': 'secret'} )
        self.assertEqual(response.status_code, 200)
