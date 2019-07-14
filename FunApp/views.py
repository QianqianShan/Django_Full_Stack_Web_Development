from django.shortcuts import render
# import templateview
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# import Post
from .models import Post
# Create your views here.
# http://ccbv.co.uk/projects/Django/2.2/django.views.generic.base/TemplateView/

# create a simple view class with TemplateView
class HelloDjango(TemplateView):
    # render the home.html file
    template_name = 'home.html'

# master interface
# add LoginRequiredMixin to make sure one needs to login before seeing contents
class PostView(LoginRequiredMixin, ListView):
    # model is Post in models.py
    model = Post
    template_name = 'posts.html'
    # login_url is an attribute, no need to use reverse() here
    login_url = 'login'

# Detail interface
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

# CreateView
class PostCreateView(CreateView):
    model = Post
    template_name = 'add_post.html'
    # required form infor, selected from Post class attributes
    fields = '__all__'
    # fields = 'title'

# UpdateView
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    # only update title
    fields = ('title',)

# DeleteView
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    # redirect to success_url when delete operation is done
    success_url = reverse_lazy('home')

# signup view
class SignupView(CreateView):
    # can have prevknown fields
    # predefined form class
    # form_class = UserCreationForm # default built-in user creation form
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
