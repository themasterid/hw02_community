from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    text = 'Главная страница'
    context = {
        'title': title,
        'text': text,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    text = 'Страница о группах проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)
