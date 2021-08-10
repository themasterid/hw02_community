# posts/urls.py
from django.urls import path

from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='group_list'),
    path('<int:pk>/', BlogListView.as_view(), name='posts'),
    path('', BlogListView.as_view(), name='posts'),
]

'''
from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index),
    # path('group/<slug>/', views.group_posts),
    path('posts/', views.index, name='posts_post'),
    path('group/', views.index, name='group_list'),
]
'''
