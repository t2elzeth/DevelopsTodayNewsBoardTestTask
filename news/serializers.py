from rest_framework import serializers

from .models import Comment, Post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author_name", "content", "creation_date"]

    def create(self, validated_data):
        validated_data.update(
            {"post": Post.objects.get(id=self.context["view"].kwargs["pk"])}
        )
        return super().create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    upvotes = serializers.IntegerField(source="upvotes.count")

    class Meta:
        model = Post
        fields = ["id", "author_name", "title", "upvotes", "creation_date"]
