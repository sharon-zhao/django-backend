from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user, authenticate, login, logout
from django.middleware.csrf import get_token
from operator import itemgetter

from ..models.comment import Comment
from ..serializers import CommentSerializer, UserSerializer

# Create your views here.
class Comments(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        """Index request"""
        # mangos = Comment.objects.all()
        comments = Comment.objects.filter(owner=request.user.id)
        data = CommentSerializer(comments, many=True).data
        return Response(data)

    serializer_class = CommentSerializer
    def post(self, request):
        """Create request"""
        # Add user to request object
        request.data['comment']['owner'] = request.user.id
        # Serialize/create mango
        comment = CommentSerializer(data=request.data['comment'])
        if comment.is_valid():
            m = comment.save()
            return Response(comment.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comment.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        comment = get_object_or_404(Comment, pk=pk)
        data = CommentSerializer(comment).data
        # Only want to show owned mangos?
        # if not request.user.id == data['owner']:
        #     raise PermissionDenied('Unauthorized, you do not own this mango')
        return Response(data)

    def delete(self, request, pk):
        """Delete request"""
        comment = get_object_or_404(Comment, pk=pk)
        data = CommentSerializer(comment).data
        if not request.user.id == data['owner']:
            raise PermissionDenied('Unauthorized, you do not own this comment')
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Remove owner from request object
        if request.data['comment'].get('owner', False):
            del request.data['comment']['owner']

        # Locate Comment
        comment = get_object_or_404(Comment, pk=pk)
        data = CommentSerializer(comment).data
        # Check if user is  the same
        if not request.user.id == data['owner']:
            raise PermissionDenied('Unauthorized, you do not own this comment')

        # Add owner to data object now that we know this user owns the resource
        request.data['comment']['owner'] = request.user.id
        # Validate updates with serializer
        ms = CommentSerializer(comment, data=request.data['comment'])
        if ms.is_valid():
            ms.save()
            print(ms)
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)
