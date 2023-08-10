from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, redirect
from .forms import ArticleForm

class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    ordering = ['-create_time']
    paginate_by = 5

class NewsDetail(DetailView):
    model = Post
    template_name = 'newsobj.html'
    context_object_name = 'newsobj'

class PostCreateView(CreateView):
    model = Post
    template_name = 'add_post.html'
    form_class = PostForm
    success_url = reverse_lazy('news:news_list')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    form_class = PostForm
    success_url = reverse_lazy('news:news_list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('news:news_list')

def search_news(request):
    title = request.GET.get('title', '')
    author = request.GET.get('author', '')
    date = request.GET.get('date', '')

    search_q = Q()
    if title:
        search_q |= Q(news_title__icontains=title)
    if author:
        search_q |= Q(post_author__username__icontains=author)
    if date:
        search_q |= Q(create_time__gt=date)

    news_list = Post.objects.filter(search_q)
    return render(request, 'search_news.html', {'news_list': news_list})

def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('name_of_the_articles_list_view')
    else:
        form = ArticleForm()
    return render(request, 'news/create_article.html', {'form': form})