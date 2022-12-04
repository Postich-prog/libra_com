from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')


# Страница со списком мороженого
def book_list(request):
    return HttpResponse('Список книг')


# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def book_detail(request, pk):
    return HttpResponse(f'Книга номер {pk}')
