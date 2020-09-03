from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.post import Post
from .models.user import User
from .models.comment import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'comments', 'owner')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)
