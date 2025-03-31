#from django.shortcuts import render
#from blogs.views import BlogListCreateView, BlogDetailView, CommentCreateView, LikeCreateView, CountryInfoView

from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import BlogPost, Comment, Like
from .serializers import BlogPostSerializer, CommentSerializer, LikeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CountryInfoView(generics.GenericAPIView):
    def get(self, request, country_name):
        response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
        return Response(response.json() if response.status_code == 200 else {"error": "Country not found"})

