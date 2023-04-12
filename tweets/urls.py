from django.urls import path

from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.TweetList.as_view(), name='tweet-list'),
    path('<int:pk>/', views.TweetDetail.as_view(), name='tweet-detail'),
    path('images/', views.TweetImageList.as_view(), name='tweetimage-list'),
    path('images/<int:pk>/', views.TweetImageDetail.as_view(), name='tweetimage-detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
