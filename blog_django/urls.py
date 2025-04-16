from django.urls import path, include
from django.contrib import admin
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('post/new/', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('search/', views.post_search, name='post_search'),

    # Добавляем маршрут для страницы с подробностями о посте
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # Главная страница (например, список постов)
    path('', views.post_list, name='post_list'),
]

# Для обработки медиафайлов (включая изображения)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

