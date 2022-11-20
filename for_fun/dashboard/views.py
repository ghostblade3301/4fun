from django.shortcuts import render


def index(request):
    template = 'dashboard/index.html'
    title = 'Главная страница'
    text = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)


def group_posts(request):
    text = 'Здесь будет информация о группах проекта Yatube'
    template = 'dashboard/group_list.html'
    context = {
        'text': text,
    }
    return render(request, template, context)
