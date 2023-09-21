from rest_framework import serializers

from .models import Comment, Forum


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'
        read_only_fields = ['author', ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'forum']
