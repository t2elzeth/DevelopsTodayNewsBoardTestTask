from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Comment, Post, Upvote
from .serializers import CommentSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(methods=["post"], detail=True)
    def upvote(self, request, pk):
        Upvote.objects.create(post=self.get_object())
        return Response(status=status.HTTP_200_OK)

    @upvote.mapping.delete
    def delete_upvote(self, request, pk):
        Upvote.objects.last().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["post"], detail=True, serializer_class=CommentSerializer)
    def comment(self, request, pk):
        return self.create(request, pk)


class CommentViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
