from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('Самая Главная страница')


def group_posts(request, slug):
    return HttpResponse(f'Страница группы {slug}')


def general_page(request):
    return HttpResponse('Главная страница всех групп')