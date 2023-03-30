from django.shortcuts import render
from rest_framework import serializers, viewsets
from .permissions import IsOwnerProfileOrReadOnly
from django.views.generic.detail import DetailView
from .models import Blog, Reviwes
from  . serializers import BlogSerializer, BlogCreateSerializer, ReviewCreateSerializer, BlogAuthorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogCreateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]
    queryset = Blog.objects.all()
    serializer_class = BlogCreateSerializer


class ReviewCreateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]
    queryset = Reviwes.objects.all()
    serializer_class = ReviewCreateSerializer


class BlogAuthorViewSet(APIView):

    def get(self, request, slug):
        articles = Blog.objects.filter(author__username=slug)
        # the many param informs the serializer that it will be serializing more than a single article.
        serializer = BlogAuthorSerializer(articles, many=True)
        return Response(serializer.data)


def main(request):
    return render(
        request,
        'crblog/main.html',
    )


def profile(request):
    return render(
        request,
        'crblog/profile.html',
    )


def create(request):
    return render(
        request,
        'crblog/create.html',
    )


def create(request):
    return render(
        request,
        'crblog/create.html',
    )


def about(request):
    return render(
        request,
        'crblog/about.html',
    )


class Blog_Detail(DetailView):
    # specify the model to use
    model = Blog

