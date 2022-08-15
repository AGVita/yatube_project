from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def index(request):
    template = 'posts/index.html'
    context = {
        'title': "Это главная страница проекта Yatube"
    }
    return render(request, template, context)
    # return HttpResponse(
    #     'Ты <i>не можешь</i> получить правильные <b>ответы</b>,<br> '
    #     'если у тебя нет правильных <s>вопросов</s> запросов.'
    # )


def group_posts(request):
    template = 'posts/group_list.html'
    context = {
        'title': "Здесь будет информация о группах проекта Yatube"
    }
    return render(request, template, context)


def general_page(request, slug):
    template = 'posts/group_list.html'
    context = {
        'title': "Здесь будет информация о группах проекта Yatube"
    }
    return render(request, template, context)