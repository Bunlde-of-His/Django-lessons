from django.contrib import admin
from django.urls import path
from .views import (
    show_base,
    show_about,
    show_topics,
    show_register,
    show_login,
    show_create_article,
    show_articles,
    show_full_articles,


)


urlpatterns = [
    path('', show_base, name='show_base'),
    path('articles/', show_articles, name='show_articles'),
    path('full_articles/', show_full_articles, name='show_full_articles'),
    path('about/', show_about, name='show_about'),
    path('topics/', show_topics, name='show_topics'),
    path('register/', show_register, name='show_register'),
    path('login/', show_login, name='show_login'),
    path('create_article/', show_create_article, name='show_create_article')
]
