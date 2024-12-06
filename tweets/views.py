import requests
from django.core.files.base import ContentFile
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from tweets.models import Tweet, TweetImage
from tweets.serializers import TweetImageSerializer, TweetSerializer
from tweets.utils import fetch_image


class TweetsView(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        images_data = request.data.get("images", [])
        for image_data in images_data:
            thumbnail_url = image_data.get("thumb")
            large_url = image_data.get("large")
            if thumbnail_url:
                try:
                    file_name, content = fetch_image(thumbnail_url)
                    image_data["thumb"] = ContentFile(content, name=file_name)
                except requests.RequestException as e:
                    return Response({"thumb": f"Failed to fetch thumbnail: {e}"}, status=status.HTTP_400_BAD_REQUEST)
            if large_url:
                try:
                    file_name, content = fetch_image(large_url)
                    image_data["large"] = ContentFile(content, name=file_name)
                except requests.RequestException as e:
                    return Response({"large": f"Failed to fetch large image: {e}"}, status=status.HTTP_400_BAD_REQUEST)
        request.data["images"] = images_data
        return super().create(request, *args, **kwargs)


class TweetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticated]


class TweetImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TweetImage.objects.all()
    serializer_class = TweetImageSerializer
    permission_classes = [IsAuthenticated]
