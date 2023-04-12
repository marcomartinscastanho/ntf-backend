from django.contrib import admin

from .models import Tweet, TweetImage


class TweetImageInline(admin.StackedInline):
    model = TweetImage
    extra = 0


class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetImageInline]


admin.site.register(Tweet, TweetAdmin)
admin.site.register(TweetImage)
