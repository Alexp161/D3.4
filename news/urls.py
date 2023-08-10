from django.urls import path
from .views import NewsList, NewsDetail, PostCreateView, PostUpdateView, PostDeleteView, search_news, create_article, ArticleListView

app_name = 'news'

urlpatterns = [
    path('', NewsList.as_view(), name='news'),
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('add/', PostCreateView.as_view(), name='add_news'),
    path('search/', search_news, name='search_results'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit_news'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete_news'),
    path('create/', create_article, name='create_article'),
    path('articles/', ArticleListView.as_view(), name='articles_list'),
]


