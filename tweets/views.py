from rest_framework import generics
from rest_framework import permissions
from tweets.models import Tweet, TweetImage
from tweets.serializers import TweetImageSerializer, TweetSerializer


class TweetList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticated]


class TweetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [permissions.IsAuthenticated]


class TweetImageList(generics.ListCreateAPIView):
    queryset = TweetImage.objects.all()
    serializer_class = TweetImageSerializer
    permission_classes = [permissions.IsAuthenticated]


class TweetImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TweetImage.objects.all()
    serializer_class = TweetImageSerializer
    permission_classes = [permissions.IsAuthenticated]
