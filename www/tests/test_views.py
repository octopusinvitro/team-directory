from django.test import Client, TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_loads_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<h1>Team Directory</h1>' in str(response.content))
