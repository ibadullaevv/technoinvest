from django.urls import path
from .views import *

app_name = 'misc'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<id>/', ArticleListByCategoryView.as_view(), name='articles_by_category'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),

    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('news/<int:pk>/', PostDetailView.as_view(), name='post_detail'),

]
