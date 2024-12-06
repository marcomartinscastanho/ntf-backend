from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from options.views import BlogDetail, BlogList, TagDetail, TagList

urlpatterns = [
    path("blogs/", BlogList.as_view(), name="blog-list"),
    path("blogs/<int:pk>/", BlogDetail.as_view(), name="blog-detail"),
    path("tags/", TagList.as_view(), name="tag-list"),
    path("tags/<int:pk>/", TagDetail.as_view(), name="tag-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
