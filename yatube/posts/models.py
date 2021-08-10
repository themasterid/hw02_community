from django.db import models


class Post(models.Model):
    text = models.TextField(max_length=700)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Пост"
    )
    group = models.ForeignKey(
        "Group",
        on_delete=models.CASCADE,
        related_name='group',
        blank=True,
        null=True,
        verbose_name="Группа"
    )


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.title
