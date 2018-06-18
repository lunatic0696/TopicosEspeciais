from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('pk', 'name', 'email', 'address')

class PostSerializer(serializers.HyperlinkedModelSerializer):

    userId = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Post
        fields = ('pk', 'title', 'body', 'userId')

class CommentSerializer(serializers.HyperlinkedModelSerializer):

    postId = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = ('pk', 'name', 'email', 'body', 'postId')