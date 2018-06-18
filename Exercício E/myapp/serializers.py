from rest_framework import serializers
from myapp.models import *


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('street', 'suite', 'city', 'zipcode')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('name', 'email', 'address',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.SlugRelatedField(queryset=Post.objects.all(), slug_field='title')

    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'post')
