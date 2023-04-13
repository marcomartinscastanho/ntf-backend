from django.contrib import admin

from .models import Tweet, TweetImage


class TweetImageInline(admin.StackedInline):
    model = TweetImage
    extra = 0


class TweetAdmin(admin.ModelAdmin):
    list_display = ['tweet_id', 'author', 'num_images', 'tweeted', 'is_posted']
    list_filter = ['author']
    readonly_fields = ['is_posted']

    inlines = [TweetImageInline]

    def is_posted(self, obj):
        return obj.is_posted
    is_posted.short_description = 'is posted'
    is_posted.boolean = True

    def num_images(self, obj):
        return len(obj.images)
    num_images.short_description = 'images'


class TweetImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'tweet_author', 'tweet_id', 'position',  'name', 'is_posted']
    list_filter = ['is_posted']

    def tweet_author(self, obj):
        return obj.tweet.author
    tweet_author.short_description = 'auhtor'

    def tweet_id(self, obj):
        return obj.tweet.tweet_id
    tweet_id.short_description = 'tweet'


admin.site.register(Tweet, TweetAdmin)
admin.site.register(TweetImage, TweetImageAdmin)
