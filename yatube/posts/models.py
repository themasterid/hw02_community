from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=700)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )


'''
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=400)
    contact = models.EmailField(max_length=254)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="events")
    location = models.CharField(max_length=400)
'''
