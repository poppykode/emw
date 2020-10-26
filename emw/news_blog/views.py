from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import BlogNews

# Create your views here.


def news_blog_detail(request, slug):
    template_name = 'news_blog/news_blog_detail.html'
    bn = BlogNews.objects.all()
    news = bn.filter(category='news').count()
    articles = bn.filter(category='articles').count()
    qs = get_object_or_404(BlogNews, slug=slug)
    return render(request, template_name, {'obj': qs, 'news': news, 'articles': articles})


def new_articles(request, type):
    template_name = 'news_blog/news_blog.html'
    qs_all = BlogNews.objects.all()
    if type != 'all':
        news_articles_list = qs_all.filter(category=type)
        paginator = Paginator(news_articles_list, 3)
        page = request.GET.get('page')
        qs = paginator.get_page(page)
        return render(request, template_name, {'obj': qs, 'type': type})
    paginator = Paginator(qs_all, 3)
    page = request.GET.get('page')
    qs = paginator.get_page(page)
    return render(request, template_name, {'obj': qs, 'type': 'NEWS & ARTICLES'})


def search_blog_news(request):
    template_name = 'news_blog/search.html'
    if request.method == 'GET':
        query = request.GET.get('q')
        if query is not None:
            lookups = Q(title__icontains=query) | Q(
                description__icontains=query) | Q(category__icontains=query)
            results_list = BlogNews.objects.filter(lookups).distinct()
            paginator = Paginator(results_list, 3)
            page = request.GET.get('page')
            results = paginator.get_page(page)
            context = {'obj': results, 'query': query}
            return render(request, template_name, context)
        else:
            return render(request, template_name)
    else:
        return render(request, template_name)
