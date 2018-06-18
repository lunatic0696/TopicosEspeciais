"""blogsapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from myapp import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.ApiRoot.as_view(),name=views.ApiRoot.name),
    path('profiles/',  views.ProfileList.as_view(), name="profile"),
    path('profiles/<int:pk>',  views.ProfileDetail.as_view(), name=views.ProfileDetail.name),
    path('posts/', views.PostList.as_view(), name = "posts"),
    path('posts/<int:pk>', views.PostDetail.as_view(), name = "post-detail"),
    path('comments/', views.CommentList.as_view(), name = "comments"),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name = "comment-detail"),
    path('api-token-auth/', obtain_auth_token),
    path('api-token-auth-custom/', views.CustomAuthToken.as_view()),
]
