
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Forum, Comment
from .serializers import ForumSerializer, CommentSerializer
from .permissions import AuthorPermission


class ForumListCreateAPIView(ListCreateAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
    authentication_classes = [TokenAuthentication, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ForumRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AuthorPermission, ]


class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication, ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, forum=Forum.objects.get(id=self.kwargs['forum_id']))

    def list(self, request, *args, **kwargs):
        comments = Comment.objects.filter(forum=self.kwargs['forum_id'])
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [AuthorPermission, ]

