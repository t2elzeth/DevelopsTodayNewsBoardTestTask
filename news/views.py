from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from .models import Comment, Post, Upvote
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    """CRUD to manage posts"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=["post"], detail=True)
    def upvote(self, request, pk):
        """Upvote specific post"""
        Upvote.objects.create(post=self.get_object())
        return self.retrieve(request, pk)

    @upvote.mapping.delete
    def delete_upvote(self, request, pk):
        """Downvote specific post"""
        upvote = Upvote.objects.last()
        if upvote is not None:
            upvote.delete()
        return self.retrieve(request, pk)

    @action(methods=["post"], detail=True, serializer_class=CommentSerializer)
    def comment(self, request, pk):
        """Leave comment on specific post"""
        return self.create(request, pk)


class CommentViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """ViewSet to retrieve, update, patch and delete comments"""

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
