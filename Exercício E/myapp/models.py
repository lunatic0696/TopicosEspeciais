from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    userDjango = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

class Address(models.Model):
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    owner = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title + ': ' + self.body

    class Meta:
        ordering = ('title',)

class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    body = models.CharField(max_length=200)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return 'Nome: ' + self.name + ', Email: ' + self.email + ', Comment: ' + self.body

    class Meta:
        ordering = ('name',)
