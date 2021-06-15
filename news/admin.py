from django.contrib import admin

from .models import Comment, Post, Upvote


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class UpvoteInline(admin.StackedInline):
    model = Upvote
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    def upvotes(self, obj):
        return obj.upvotes.count()

    readonly_fields = ["id", "creation_date", "upvotes"]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "id",
                    "creation_date",
                    "upvotes",
                    "author_name",
                    "title",
                )
            },
        ),
    )

    list_filter = [
        "creation_date",
    ]

    inlines = [CommentInline, UpvoteInline]


admin.site.register(Upvote)
