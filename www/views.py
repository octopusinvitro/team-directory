from django.shortcuts import render

from .helpers import Pagination, INDEX_PAGE_MAX_ITEMS
from .models import Person


def index(request):
    pagination = Pagination(Person.objects.all(), INDEX_PAGE_MAX_ITEMS)
    return render(
        request, 'index.html', {'current_page': pagination.items_for_page(1)})


def index_page(request, page):
    pagination = Pagination(Person.objects.all(), INDEX_PAGE_MAX_ITEMS)
    return render(
        request, 'index.html', {'current_page': pagination.items_for_page(page)})
