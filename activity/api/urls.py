from django.urls import path

from activity.api.views import LikeCreateAPIVew, CommentCreateAPIView

urlpatterns = [
    path('like/post<int:pk>', LikeCreateAPIVew.as_view()),
    path('comment/post<int:pk>', CommentCreateAPIView.as_view()),
]
