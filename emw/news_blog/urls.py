from django.urls import path
from .views import (
    news_blog_detail,
    search_blog_news,
    new_articles
)


app_name = 'news_blog'
urlpatterns = [
    path('media/<slug:slug>', news_blog_detail, name='news_blog_detail'),
    path('<str:type>', new_articles, name='new_articles'),
    path('search', search_blog_news, name='search_blog_news'),

]
