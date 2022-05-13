from django.views.generic import ListView
from . models import Post,News


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class NewsView(ListView):
    model = News
    template_name = 'about.html'
