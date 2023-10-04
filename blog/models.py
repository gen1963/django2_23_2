from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name="Категорія")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"


class Post(models.Model):
    title = models.CharField(max_length=30, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published = models.DateTimeField(auto_created=True, verbose_name="Дата та час")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    image = models.URLField(default="http://placehold.it/900x300")
    # comments = models.ForeignKey(Comment, verbose_name='Коментарі')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Пости"

# class Comment(models.Model):
#     user_name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
#     description = models.TextField(verbose_name="Коментар")
#     date_comment = models.DateTimeField(auto_created=True, verbose_name="Дата та час")
#
#
#     def __str__(self):
#         return self.user_name
#
#     class Meta:
#         verbose_name = "Коментар"
#         verbose_name_plural = "Коментарі"

class Comments_post(models.Model):
    email = models.EmailField()
    user_name = models.CharField(max_length=30, verbose_name="Автор")
    description = models.TextField(max_length=1000, verbose_name="Коментар")
    date_comments = models.DateTimeField(auto_created=True, verbose_name="Дата та час")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')

    def __str__(self):
        return f'{self.user_name}, {self.post}'

    class Meta:
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"

class Photo(models.Model):
    image = models.ImageField(upload_to='uploads', verbose_name="Фото")
    description = models.CharField(max_length=50, verbose_name="Опис")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Пост")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"