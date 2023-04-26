from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings
from .models import Book


def index(request):
    post_list = Book.objects.order_by('-id')
    paginator = Paginator(post_list, settings.POST_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'book/index.html', context)


def author(request):
    template = 'about/author.html'
    return render(request, template)
