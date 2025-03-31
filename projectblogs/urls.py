"""
URL configuration for projectblogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from blogs.views import BlogListCreateView, BlogDetailView, CommentCreateView, LikeCreateView, CountryInfoView
from django.contrib.auth.models import User
User.objects.create_user(username="user1", password="pass123")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogs/', BlogListCreateView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('comments/', CommentCreateView.as_view(), name='comment-create'),
    path('likes/', LikeCreateView.as_view(), name='like-create'),
    path('countries/<str:country_name>/', CountryInfoView.as_view(), name='country-info'),
]
