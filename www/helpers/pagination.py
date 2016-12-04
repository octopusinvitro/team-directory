from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class Pagination:
    def __init__(self, objects, amount):
        self.paginator = Paginator(objects, amount)

    def items_for_page(self, page):
        try:
            items = self.paginator.page(page)
        except PageNotAnInteger:
            items = self.paginator.page(1)
        except EmptyPage:
            items = self.paginator.page(self.paginator.num_pages)

        return items
