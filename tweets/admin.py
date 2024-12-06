from django.contrib import admin
from django.db.models import Q

from tweets.models import Tweet, TweetImage


class TweetImageInline(admin.StackedInline):
    model = TweetImage
    extra = 0


class TweetAdmin(admin.ModelAdmin):
    list_display = ["id", "author", "num_images", "tweeted", "is_posted"]
    list_filter = ["author"]
    search_fields = ("id",)
    readonly_fields = ["is_posted"]

    inlines = [TweetImageInline]

    def is_posted(self, obj):
        return obj.is_posted

    is_posted.short_description = "is posted"
    is_posted.boolean = True

    def num_images(self, obj):
        return len(obj.images.all())

    num_images.short_description = "images"


class IsPostedFilter(admin.SimpleListFilter):
    title = "is posted"
    parameter_name = "is_posted"

    def lookups(self, request, model_admin):
        return (("True", True), ("False", False))

    def queryset(self, request, queryset):
        if self.value() == "True":
            return queryset.filter(post__isnull=False)
        elif self.value() == "False":
            return queryset.filter(post__isnull=True)


class HasImageFilter(admin.SimpleListFilter):
    title = "has image"
    parameter_name = "has_image"

    def lookups(self, request, model_admin):
        return (("True", True), ("False", False))

    def queryset(self, request, queryset):
        if self.value() == "True":
            return queryset.filter(~Q(thumbnail="") & ~Q(large_image=""))
        elif self.value() == "False":
            return queryset.filter(
                Q(thumbnail="") | Q(large_image="") | Q(thumbnail__isnull=True) | Q(large_image__isnull=True)
            )


class TweetImageAdmin(admin.ModelAdmin):
    list_display = ["id", "tweet_author", "tweet_id", "position", "name", "post", "is_posted"]
    list_filter = [
        HasImageFilter,
        IsPostedFilter,
        "tweet__author",
    ]
    search_fields = ("id",)

    def tweet_author(self, obj):
        return obj.tweet.author

    tweet_author.short_description = "auhtor"

    def tweet_id(self, obj):
        return obj.tweet.id

    tweet_id.short_description = "tweet"


admin.site.register(Tweet, TweetAdmin)
admin.site.register(TweetImage, TweetImageAdmin)
