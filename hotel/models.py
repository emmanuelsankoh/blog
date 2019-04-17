from django.db import models
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=25)
    post = models.TextField()
    cover = models.FileField()

    def get_absolute_url(self):
        return reverse('hotel:index')


class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    comment=models.TextField()
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)

    def get_absolute_url(self):
        return reverse('hotel:comment', args=[str(self.pk)])









