from bs4 import BeautifulSoup
from django.test import Client, TestCase

from www.helpers import INDEX_PAGE_MAX_ITEMS
from www.models import Person


class PaginationTest(TestCase):
    def setUp(self):
        self.client = Client()
        for i in range(INDEX_PAGE_MAX_ITEMS + 1):
            Person.objects.create(
                name='name', email='email', title='title', image='image')

    def test_first_page_has_no_link_to_previous(self):
        response = self.client.get('/')
        self.assertNotIn('previous', str(response.content))
        self.assertIn('next', str(response.content))

    def test_last_page_has_no_link_to_next(self):
        response = self.client.get('/2/')
        self.assertIn('previous', str(response.content))
        self.assertNotIn('next', str(response.content))

    def test_next_links_to_next_page(self):
        response = self.client.get('/')
        soup = BeautifulSoup(str(response.content), "html.parser")
        next_link = soup.find(class_='nopagenumber').find('a')
        self.assertEqual(next_link['href'], '/2/')

    def test_previous_links_to_previous_page(self):
        response = self.client.get('/2/')
        soup = BeautifulSoup(str(response.content), "html.parser")
        next_link = soup.find(class_='nopagenumber').find('a')
        self.assertEqual(next_link['href'], '/1/')

    def test_pagination_shows_all_pages(self):
        response = self.client.get('/')
        soup = BeautifulSoup(str(response.content), "html.parser")
        li = soup.find_all('li', class_='pagenumber')
        self.assertEqual(len(li), 2)

    def test_pagination_marks_current_page_for_screenreaders(self):
        response = self.client.get('/')
        soup = BeautifulSoup(str(response.content), "html.parser")
        current = soup.find(class_='pagination').find(class_='active')
        self.assertIn('(current)', current.text)

    def test_page_is_linked_if_not_current(self):
        response = self.client.get('/2/')
        soup = BeautifulSoup(str(response.content), "html.parser")
        link = soup.find(class_='pagenumber').find('a')
        self.assertEqual(link['href'], '/1/')
