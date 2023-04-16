from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'tweet', 'source', 'num_images', 'rating', 'blog', 'is_posted']

    def num_images(self, obj):
        return len(obj.images.all())
    num_images.short_description = 'images'


admin.site.register(Post, PostAdmin)
