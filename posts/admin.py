from django.contrib import admin

from posts.models import Post
from tweets.admin import TweetImageInline


class IsPostedFilter(admin.SimpleListFilter):
    title = "is posted"
    parameter_name = "is_posted"

    def lookups(self, request, model_admin):
        return (("True", True), ("False", False))

    def queryset(self, request, queryset):
        if self.value() == "True":
            return queryset.filter(nt_post_id__isnull=False)
        elif self.value() == "False":
            return queryset.filter(nt_post_id__isnull=True)


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "tweet", "source", "num_images", "rating", "blog", "is_posted"]
    readonly_fields = [
        "id",
        "comment",
        "tweet",
        "source",
        "num_images",
        "rating",
        "blog",
        "is_posted",
        "nt_post_id",
        "tags",
        "queue",
    ]
    list_filter = [IsPostedFilter]
    search_fields = ("id",)
    inlines = (TweetImageInline,)

    def num_images(self, obj):
        return len(obj.images.all())

    num_images.short_description = "images"


admin.site.register(Post, PostAdmin)
