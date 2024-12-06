from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tweets.views import TweetDetailView, TweetImageDetailView, TweetsView

urlpatterns = [
    path("", TweetsView.as_view(), name="create-or-list-tweets"),
    path("<int:pk>/", TweetDetailView.as_view(), name="tweet-detail"),
    path("images/<int:pk>/", TweetImageDetailView.as_view(), name="get-update-delete-tweetimage"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
