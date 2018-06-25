from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.throttling import *
from myapp.serializers import *
from myapp import permissions as customPermissions


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-list'
    permission_classes = (customPermissions.IsAuthenticatedReadOnly,)


class ProfileDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'
    permission_classes = (permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        profile = Profile.objects.get(userDjango = self.request.user)
        serializer.save(owner=profile)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'
    permission_classes = (customPermissions.PostPermission,)

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'

class CustomAuthToken(ObtainAuthToken):
    throttle_scope = 'api-token-auth-custom'
    throttle_classes = (ScopedRateThrottle,)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
        context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
})


class ApiRoot(generics.GenericAPIView):

    name = 'api-root'

    def get(self, request,*args, **kwargs):
        return Response({
            'profiles': reverse('profile', request=request),
            'posts': reverse('posts', request=request),
            'comments': reverse('comments', request=request)

        })