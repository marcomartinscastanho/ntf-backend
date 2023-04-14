from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.PostList.as_view(), name='post-list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
