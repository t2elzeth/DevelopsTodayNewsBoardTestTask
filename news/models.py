from django.db import models


class Post(models.Model):
    author_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post #{self.title[:20]} by {self.author_name}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author_name = models.CharField(max_length=255)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on post#{self.post.id} by {self.author_name}"


class Upvote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="upvotes")

    def __str__(self):
        return f"Upvote for post#{self.post.id}"
