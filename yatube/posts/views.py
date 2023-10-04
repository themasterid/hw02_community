from django.conf import settings
from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    """Выводим на страницу первые 10 записей постов."""

    posts = Post.objects.select_related('author')[:settings.POSTS_PAGE]
    return render(request, 'posts/index.html', {'posts': posts})


def group_posts(request, slug):
    """Выводим на страницу первые 10 записей групп."""

    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')[:settings.GROUPS_PAGE]
    return render(request, 'posts/group_list.html', {'group': group, 'posts': posts})
