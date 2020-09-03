from django.db import models
from .user import User
from .post import Post
# Create your models here.
class Comment(models.Model):
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name = 'comments',
        null=True,
        on_delete=models.CASCADE
    )
    objects = models.Manager()


    def __str__(self):
        return self.body
