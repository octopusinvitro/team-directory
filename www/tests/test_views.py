from django.test import Client, TestCase

from www.helpers import INDEX_PAGE_MAX_ITEMS
from www.models import Person


class HomeTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_loads_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<h1>Team Directory</h1>' in str(response.content))

    def test_loads_home_page_number(self):
        for i in range(INDEX_PAGE_MAX_ITEMS + 1):
            Person.objects.create(
                name='name', email='email', title='title', image='image')
        response = self.client.get('/2/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Page 2 of 2.' in str(response.content))
