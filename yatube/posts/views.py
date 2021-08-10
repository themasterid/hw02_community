from django.views.generic import ListView, DetailView
#from django.shortcuts import render
from .models import Post, Group


class BlogListView(ListView):
    model = Post
    paginate_by = 3
    template_name = 'base.html'


class BlogDetailView(DetailView):
    model = Group
    template_name = 'group_detail.html'


'''
from .models import Post, Group

from django.shortcuts import render, get_object_or_404


def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    posts = Post.objects.order_by('-pub_date')[:10]
    text = 'Последние обновления на сайте'
    context = {
        'title': title,
        'text': text,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
'''
