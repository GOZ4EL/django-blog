from django.test import TestCase
from django.urls import reverse

from articles.models import Article

class ArticleListView(TestCase):
    """Article List View testing class (Home View)"""
    def test_view_url_exists_at_desired_location(self):
        """The Article list view exists at '/' location."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """The Article list view can be accessible by its name: 'home'."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """The Article list view uses the desired template."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class ArticleDetailView(TestCase):
    """Article Detail View Testing Class"""
    def test_view_url_exists_at_desired_location(self):
        article = Article.object.create()
        response = self.client.get(revers('detail', args=()))
