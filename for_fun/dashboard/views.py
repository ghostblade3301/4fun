from django.http import HttpResponse

# from django.shortcuts import render


def index(request):
    return HttpResponse('<h1 align=center>Главная страница</h1><p><h3>Добро пожаловать на наш сайт</h3></p>')


def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')


def group_posts(request):
    return HttpResponse('<h1>Страница групп</h1>')
