from django.test import TestCase
from django.urls import reverse

from django.contrib.auth.models import User
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
    def test_view_default_article(self):
        user = User.objects.create(username="authuser", password="sahfdsau1324$9'%")
        article = Article.objects.create(
            author=user, title="Test Art.", body="Lorem Ipsum dolor."
        )
        response = self.client.get(reverse('detail', args=(article.id,)))
        self.assertContains(response, article.title)
        self.assertContains(response, article.body)

