from django.views.generic import ListView, DetailView
from . models import Article

class ArticleListView(ListView):
    """List View for Article Model"""
    model = Article
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    """Detail View for Article Model"""
    model = Article
    template_name = 'detail.html'
