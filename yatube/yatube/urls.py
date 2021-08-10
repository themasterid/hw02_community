# yatube/urls.py
from django.contrib import admin 
from django.urls import path, include


urlpatterns = [
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
]

'''
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls'), name='index'),
    path('posts/', include('posts.urls'), name='posts_post'),
    path('group/', include('posts.urls'), name='group_list'),
    path('admin/', admin.site.urls),
]
'''
