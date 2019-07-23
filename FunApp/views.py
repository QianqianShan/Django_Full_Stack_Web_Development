from annoying.decorators import ajax_request

from django.shortcuts import render
# import templateview
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
# import Post
from .models import Post, FunAppUser, Like
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


class UserDetail(DetailView):
    model = FunAppUser
    template_name = 'user_profile.html'
    login_url = reverse_lazy('login')

class EditProfile(UpdateView):
    model = FunAppUser
    template_name = 'edit_profile.html'
    # users can update profile picture and username
    fields = ['profile_pic', 'username']
    login_url = reverse_lazy('login')


# function views
@ajax_request
def toggleFollow(request):
    current_user = InstaUser.objects.get(pk=request.user.pk)
    follow_user_pk = request.POST.get('follow_user_pk')
    follow_user = InstaUser.objects.get(pk=follow_user_pk)

    try:
        if current_user != follow_user:
            if request.POST.get('type') == 'follow':
                connection = UserConnection(creator=current_user, following=follow_user)
                connection.save()
            elif request.POST.get('type') == 'unfollow':
                UserConnection.objects.filter(creator=current_user, following=follow_user).delete()
            result = 1
        else:
            result = 0
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'type': request.POST.get('type'),
        'follow_user_pk': follow_user_pk
    }

@ajax_request
def addLike(request):
    # post_pk was passed from create_like in index.js file
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post = post, user = request.user)
        # save to database
        like.save()
        # write successfully --> result = 1
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0
    # return json type data
    return {
        'result': result,
        'post_pk': post_pk
    }


@ajax_request
def addComment(request):
    comment_text = request.POST.get('comment_text')
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    commenter_info = {}

    try:
        comment = Comment(comment=comment_text, user=request.user, post=post)
        comment.save()

        username = request.user.username

        commenter_info = {
            'username': username,
            'comment_text': comment_text
        }

        result = 1
    except Exception as e:
        print(e)
        result = 0

    return {
        'result': result,
        'post_pk': post_pk,
        'commenter_info': commenter_info
    }
