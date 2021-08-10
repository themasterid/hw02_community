# yatube/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('posts.urls'), name='index'),
    path('posts/', include('posts.urls'), name='posts'),
    path('group/', include('posts.urls'), name='group'),
    path('admin/', admin.site.urls),
]
