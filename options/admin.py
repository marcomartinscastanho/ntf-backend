from django.contrib import admin
from .models import Blog, Tag


class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'genres_list', 'num_posts']

    def genres_list(self, obj):
        from django.utils.safestring import mark_safe
        from django.shortcuts import resolve_url
        from django.contrib.admin.templatetags.admin_urls import admin_urlname
        from django.urls import reverse

        # urls = []
        # for genre in obj.genres.all():
        #     url = resolve_url(admin_urlname(Tag._meta, 'change'), genre.pk)
        #     urls.append(mark_safe('<a href="{}">{}</a>'.format(url, genre.name)))
        # return ", ".join(urls)

        return ", ".join([str(g) for g in obj.genres.all()])
    genres_list.short_description = 'genres'


admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag, TagAdmin)
