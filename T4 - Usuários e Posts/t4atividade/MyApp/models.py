from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=200)
    suite = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.ForeignKey('Address',related_name='Address',on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    userId = models.ForeignKey('User',related_name='Id',on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    body = models.CharField(max_length=5000)
    postId = models.ForeignKey(Post,related_name='Id',on_delete=models.CASCADE)