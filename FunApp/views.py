from django.shortcuts import render
# import templateview
from django.views.generic import TemplateView, ListView, DetailView
# import Post
from .models import Post
# Create your views here.
# http://ccbv.co.uk/projects/Django/2.2/django.views.generic.base/TemplateView/

# create a simple view class with TemplateView
class HelloDjango(TemplateView):
    # render the home.html file
    template_name = 'home.html'

# master interface
class PostView(ListView):
    # model is Post in models.py
    model = Post
    template_name = 'posts.html'

# Detail interface
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
