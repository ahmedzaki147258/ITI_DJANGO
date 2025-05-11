from rest_framework import serializers
from .models import Author, Post, Comment

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'author_id', 'created_at']

    def create(self, validated_data):
        author_id = validated_data.pop('author_id')
        author = Author.objects.get(pk=author_id)
        return Post.objects.create(author=author, **validated_data)

class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)
    posted_by = AuthorSerializer(read_only=True)
    post_id = serializers.IntegerField(write_only=True)
    posted_by_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'post_id', 'content', 'posted_by', 'posted_by_id', 'created_at']

    def create(self, validated_data):
        post_id = validated_data.pop('post_id')
        post = Post.objects.get(pk=post_id)
        posted_by_id = validated_data.pop('posted_by_id')
        posted_by = Author.objects.get(pk=posted_by_id)
        return Comment.objects.create(post=post, posted_by=posted_by, **validated_data)
