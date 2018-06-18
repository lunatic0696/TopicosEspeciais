from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import *
from rest_framework.reverse import reverse
from MyApp.serializers import *


class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-list'


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	name = 'user-detail'


class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	name = 'post-list'


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	name = 'post-detail'


class CommentList(generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	name = 'comment-list'


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	name = 'comment-detail'


class ApiRoot(generics.GenericAPIView):
	name = 'api-root'
	def get(self, request,*args,**kwargs):
		return Response({
			'user-list': reverse(UserList.name,request=request),
			'post-list': reverse(PostList.name,request=request),
			'comment-list': reverse(CommentList.name,request=request),
			})