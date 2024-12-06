from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from posts.views import PostDetail, PostList

urlpatterns = [
    path("", PostList.as_view(), name="post-list"),
    path("<int:pk>/", PostDetail.as_view(), name="post-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
