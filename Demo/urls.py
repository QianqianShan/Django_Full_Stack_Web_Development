"""Demo URL Configuration

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
from FunApp.views import SignupView, UserDetail, EditProfile, addLike

urlpatterns = [
    path('admin/', admin.site.urls),
    # include another urlconf
    path('', include('FunApp.urls')),
    # if .../auth/, use auth app urls login.html in templates/registration
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/signup/', SignupView.as_view(), name = 'signup'),
    path('user/<int:pk>/', UserDetail.as_view(), name = 'user_profile'),
    path('edit_profile/<int:pk>/', EditProfile.as_view(), name = 'edit_profile'),
    path('like', addLike, name = 'like')
]
