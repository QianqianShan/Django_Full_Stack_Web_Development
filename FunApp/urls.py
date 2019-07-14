"""FunApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from . import views

from FunApp.views import PostView, PostDetailView, PostCreateView, PostUpdateView
from FunApp.views import PostDeleteView
urlpatterns = [
    # path('', views.HelloDjango.as_view()),
    path('', PostView.as_view(), name = 'home'),
    # <int:pk> pattern match
    # set name as 'post_detail'
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post_detail'),
    path('add_post/', PostCreateView.as_view(), name = 'make_post'),
    path('update_post/<int:pk>/', PostUpdateView.as_view(), name = 'update_post'),
    path('delete_post/<int:pk>/', PostDeleteView.as_view(), name = 'delete_post')
]
