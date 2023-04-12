from django.urls import path

from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.TweetList.as_view()),
    path('<int:pk>/', views.TweetDetail.as_view()),
    path('images/', views.TweetImageList.as_view()),
    path('images/<int:pk>/', views.TweetImageDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
