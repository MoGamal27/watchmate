from rest_framework import serializers
from watchlist_app.models import Review, WatchList


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Review
        exclude = ('watchlist',)
        
        
        
class WatchListSerializer(serializers.ModelSerializer):
    platform = serializers.CharField(source='platform.name')
    
    class Meta:
        model = WatchList
        fields = "__all__"
    