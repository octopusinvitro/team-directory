from django.test import Client, TestCase
from www.models import Person


class ListPersonsTest(TestCase):
    def setUp(self):
        self.client = Client()
        Person.objects.create(
            name='name1', email='email1', title='title1', image='image1')
        Person.objects.create(
            name='name2', email='email2', title='title2', image='image2')

    def test_home_page_receives_all_persons(self):
        response = self.client.get('/')
        self.assertTrue('name1' in str(response.content))
        self.assertTrue('name2' in str(response.content))

    def test_list_shows_all_fields_for_a_person(self):
        response = self.client.get('/')
        self.assertTrue('name1' in str(response.content))
        self.assertTrue('title1' in str(response.content))
        self.assertTrue('email1' in str(response.content))
        self.assertTrue('image1' in str(response.content))
