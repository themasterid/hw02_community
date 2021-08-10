# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('group/<slug:slug>/', views.group_posts, name='group_list'),
    # ! path('posts/', views.index, name='posts'), дубляж !
]
