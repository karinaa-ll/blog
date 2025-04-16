from django.contrib import admin
from .models import Category, Tag, Post, Comment

# Регистрация модели Category в админке
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Показываем только поле name в списке
    search_fields = ('name',)  # Добавляем поиск по полю name

# Регистрация модели Tag в админке
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Показываем только поле name в списке
    search_fields = ('name',)  # Добавляем поиск по полю name

# Регистрация модели Post в админке
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'published_at')  # Показываем важные поля в списке
    list_filter = ('status', 'categories', 'tags')  # Добавляем фильтрацию по статусу, категориям и тегам
    search_fields = ('title', 'content', 'author__username')  # Добавляем поиск по этим полям
    date_hierarchy = 'published_at'  # Даем возможность фильтровать по дате публикации

# Регистрация модели Comment в админке
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'status', 'created_at')  # Показываем важные поля в списке
    list_filter = ('status', 'created_at')  # Добавляем фильтрацию по статусу и дате создания
    search_fields = ('author', 'content')  # Добавляем поиск по этим полям

# Регистрируем модели с настроенными администраторами
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
