from rest_framework import serializers

from .models import Comment, Post, PostImage


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author_name", "content", "creation_date"]

    def create(self, validated_data):
        validated_data.update(
            {"post": Post.objects.get(id=self.context["view"].kwargs["pk"])}
        )
        return super().create(validated_data)


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ["image"]


class PostSerializer(serializers.ModelSerializer):
    upvotes = serializers.IntegerField(source="upvotes.count", read_only=True)
    image = serializers.ListField(required=False, write_only=True)
    images = PostImageSerializer(required=False, many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "author_name",
            "title",
            "body",
            "upvotes",
            "creation_date",
            "images",
            "image",
        ]

    def create(self, validated_data: dict):
        images = validated_data.pop("image", None)

        post = super().create(validated_data)
        if images is not None:
            for image in images:
                post.images.create(image=image)

        return post
