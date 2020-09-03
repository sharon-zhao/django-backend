from django.db import models
from .user import User
# from s3direct.fields import S3DirectField
# from .comment import Comment
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey('User', related_name = 'user', on_delete=models.CASCADE)
    # comment_id = models.ForeignKey('Comment', related_name = 'comments', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.body}"
