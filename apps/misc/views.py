from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.db.models import Q

from .models import *



class HomeView(ListView):
    model = Slider
    template_name = 'pages/home.html'
    context_object_name = 'sliders'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['last_works'] = Article.published.all()
        context['posts'] = Post.published.all()
        return context


class ArticleListByCategoryView(ListView):
    ordering = 'id'
    # paginate_by = 10
    template_name = 'pages/articles-by-category.html'

    def get_queryset(self):
        # https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/#dynamic-filtering
        # self.category = Category.objects.get(slug=self.kwargs['slug'])
        self.category = Category.objects.get(id=self.kwargs['id'])
        queryset = Article.objects.filter(category=self.category)
        queryset = queryset.order_by(self.ordering)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'pages/article-detail.html'
    context_object_name = 'article'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_articles'] = Article.published.filter(category=self.object.category).exclude(
            id=self.object.id)
        return context


class SearchResultsListView(ListView):
    model = Article
    template_name = 'search/search-result.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Article.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'pages/post-detail.html'
