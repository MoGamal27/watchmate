from django.urls import path
from watchlist_app.api.views import UserReview


urlpatterns = [
    path('reviews/', UserReview.as_view(), name='user-review-detail'),
 ]
