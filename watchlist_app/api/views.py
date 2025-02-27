from rest_framework import generics
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from watchlist_app.models import WatchList, StreamPlatform, Review


class UserReview(generics.ListAPIView):
    
    serializer_class = ReviewSerializer
    
    
    def get_queryset(self):
        user = self.request.query_params.get('username', None)
        return Review.objects.filter(review_user__username=user)
    


 