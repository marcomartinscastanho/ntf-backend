from django.contrib import admin
from django.contrib.admin import StackedInline
from django.utils.html import format_html

from options.models import Blog, Tag
from posts.models import Post


class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]


class PostInline(StackedInline):
    extra = 0
    model = Post.tags.through
    fields = (
        "source",
        "images",
    )
    readonly_fields = (
        "source",
        "images",
    )

    def source(self, obj=None, *args, **kwargs):
        return format_html('<a href="{}" target="_blank"/>{}</a>', obj.post.source, obj.post.source)

    def images(self, obj=None, *args, **kwargs):
        post_images = obj.post.images.all()
        if not post_images.exists():
            return None
        html_content = "<div>"
        print("images: ", obj.post.images.all())
        for image in post_images:
            html_content += format_html(
                '<a href="{}" target="_blank">' '<img src="{}" style="max-height: 300px; max-width: 300px;" /></a>',
                image.large_image.url,
                image.thumbnail.url,
            )
        html_content += "</div>"
        print("html_content: ", html_content)
        return format_html(html_content)


class TagAdmin(admin.ModelAdmin):
    inlines = (PostInline,)
    list_display = ["name", "genres_list", "num_posts"]

    def genres_list(self, obj):
        return ", ".join([str(g) for g in obj.genres.all()])

    genres_list.short_description = "genres"


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
