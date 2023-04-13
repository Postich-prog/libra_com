from django.shortcuts import render


def index(request):
    template = 'library/index.html'
    return render(request, template)


def author(request):
    template = 'about/author.html'
    return render(request, template)
