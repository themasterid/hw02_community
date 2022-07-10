from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    """Выводим на страницу первые 10 записей постов."""

    posts = Post.objects.select_related('author')[:10]
    template = 'posts/index.html'
    context = {'posts': posts}
    return render(request, template, context)


def group_posts(request, slug):
    """Выводим на страницу первые 10 записей групп."""

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')[:10]
    template = 'posts/group_list.html'
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)
