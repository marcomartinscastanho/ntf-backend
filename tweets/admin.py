from django.contrib import admin

from .models import Tweet, TweetImage


class TweetImageInline(admin.StackedInline):
    model = TweetImage
    extra = 0


class TweetAdmin(admin.ModelAdmin):
    list_display = ['tid', 'tweeted', 'is_posted']
    readonly_fields = ['is_posted']

    inlines = [TweetImageInline]

    def is_posted(self, obj):
        return obj.is_posted
    is_posted.short_description = 'is posted'
    is_posted.boolean = True


class TweetImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'tweet_tid', 'name', 'is_posted']

    def tweet_tid(self, obj):
        return obj.tweet.tid
    tweet_tid.short_description = 'tweet'


admin.site.register(Tweet, TweetAdmin)
admin.site.register(TweetImage, TweetImageAdmin)
