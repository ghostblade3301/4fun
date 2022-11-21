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
    text2 = ('Вчера Крокодил<br>улыбнулся так злобно,<br>Что мне до сих '
            'пор<br>за него неудобно.<br><i>Рената Муха</i>')
    text = 'Здесь будет информация о группах проекта Yatube'
    template = 'dashboard/group_list.html'
    context = {
        'text': text,
        'text2': text2
    }
    return render(request, template, context)
