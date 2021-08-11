from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:10]
    title = 'Последние обновления на сайте'
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.order_by('group')[:10]
    title = f'Записи сообщества <{group}>'
    context = {
        'group': group,
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)
