from django.test import SimpleTestCase
from www.helpers import Pagination


class PaginationTest(SimpleTestCase):
    def setUp(self):
        self.objects = ['foo', 'bar', 'qux', 'foo', 'bar', 'qux']
        self.pagination = Pagination(self.objects, 2)

    def test_has_three_pages(self):
        self.assertEqual(
            self.pagination.paginator.num_pages, 3)

    def test_returns_items_of_second_page(self):
        self.assertEqual(
            self.pagination.items_for_page(2).object_list, ['qux', 'foo'])

    def test_returns_first_page_if_page_is_not_number(self):
        self.assertEqual(
            self.pagination.items_for_page(None).object_list, ['foo', 'bar'])

    def test_returns_last_page_if_page_is_out_of_range(self):
        self.assertEqual(
            self.pagination.items_for_page(0).object_list, ['bar', 'qux'])
        self.assertEqual(
            self.pagination.items_for_page(4).object_list, ['bar', 'qux'])
