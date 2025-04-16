from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Модель категории для поста
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Модель тега для поста
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Модель поста
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    categories = models.ManyToManyField(Category, related_name='posts', blank=True)  # Связь с категориями
    tags = models.ManyToManyField(Tag, related_name='posts', blank=True)  # Связь с тегами
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)

    def __str__(self):
        return self.title

    # Опционально, можно добавить методы для фильтрации по статусу и дате публикации
    def is_published(self):
        return self.status == 'published'

    def publish(self):
        self.status = 'published'
        self.published_at = timezone.now()
        self.save()


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active')

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'