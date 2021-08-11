from django.contrib.auth import get_user_model

from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(max_length=400)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name='group'
    )

    class Meta:
        ordering = ['-pub_date']
