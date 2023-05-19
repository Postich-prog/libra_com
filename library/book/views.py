from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm
from .models import Book
from django.http import JsonResponse


def index(request):
    post_list = Book.objects.order_by('-id')
    paginator = Paginator(post_list, settings.POST_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.user.is_authenticated:
        favorite_post_list = Book.objects.filter(users=request.user)
        context = {
            'page_obj': page_obj,
            'favorite_post_list': favorite_post_list,
        }
        return render(request, 'book/index.html', context)
    context = {
            'page_obj': page_obj,
        }
    return render(request, 'book/index.html', context)


def author(request):
    template = 'about/author.html'
    return render(request, template)


def post_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = CommentForm()
    comments = book.comments.all()
    genres = book.genres.all()
    context = {
        'books': book,
        'form': form,
        'comments': comments,
        'genres': genres,
    }
    return render(request, 'book/book_detail.html', context)


@login_required
def add_comment(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    form = CommentForm(request.POST or None)
    if request.is_ajax():
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.book = book
            comment.save()
            return JsonResponse({"book": comment.book.pk}, status=200)
    return redirect('book:book_detail', book_id=book_id)


@login_required
def add_to_favorite(request, book_id):
    if request.user.is_authenticated:
        user = request.user
        user.favorite_books.add(get_object_or_404(Book, pk=book_id))
        return redirect('book:index')
    return redirect('users:login')


@login_required
def delete_from_favorite(request, book_id):
    following = Book.objects.filter(pk=book_id)
    if following.exists():
        request.user.favorite_books.remove(get_object_or_404(Book, pk=book_id))
    return redirect('book:index')


@login_required
def favorites(request):
    user = request.user
    post_list = user.favorite_books.all()
    paginator = Paginator(post_list, settings.POST_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'book/favorites.html', context)
