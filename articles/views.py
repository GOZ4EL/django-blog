from django.views.generic import ListView
from django.models import Article

class ArticleListView(ListView):
    """List View for Article Model"""
    model = Article
    template_name = 'home.html'

