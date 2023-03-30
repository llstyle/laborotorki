from rest_framework import serializers
from .models import Blog, Reviwes

class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviwes
        fields = "__all__"
        lookup_field = 'blog'


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Reviwes
        fields = ("author", "text", "parents")


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Blog
        fields = "__all__"


class BlogAuthorSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = "__all__"


