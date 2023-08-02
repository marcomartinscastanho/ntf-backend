from rest_framework import generics, permissions
from rest_framework.response import Response
from tweets.models import TweetImage
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        unposted_images = TweetImage.objects.filter(post__isnull=True)
        posted_images = request.data.get("images", [])

        try:
            first_posted_img = posted_images[0]
            first_posted_img_idx = next((index for (index, unposted_image) in enumerate(
                unposted_images) if unposted_image.id == first_posted_img), None)
            if first_posted_img_idx == 0:
                first_posted_img_idx = len(unposted_images) - len(posted_images)
            step = first_posted_img_idx % 7
            step = step if step != 0 else 7
            next_img_idx = first_posted_img_idx - step
            next_img = unposted_images[next_img_idx]
            data = {"next": next_img.tweet.id}
        except Exception:
            data = {}

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        super().create(request, *args, **kwargs)
        return Response({**serializer.data, **data}, status=201)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
