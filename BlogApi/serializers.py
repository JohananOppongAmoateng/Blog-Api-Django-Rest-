from .models import Post,Comments
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username"]
        
        
class CommentsSerializer(serializers.ModelSerializer):
    creator = UserSerializer()
    class Meta:
        model = Comments
        fields = ["created","updated","creator","text","post"]
        
class PostSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    author = UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ["author","title","body","created","updated","published","comments"]
  