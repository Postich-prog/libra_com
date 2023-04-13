from django.shortcuts import render


def index(request):
    template = 'about/author.html'
    return render(request, template)
