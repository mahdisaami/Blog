from django.urls import path

from activity.api.views import LikeCreateAPIVew, CommentCreateAPIView, CommentListAPIView

urlpatterns = [
    path('like/post<int:pk>', LikeCreateAPIVew.as_view()),
    path('comment/post<int:pk>', CommentCreateAPIView.as_view()),
    path('comments/post<int:pk>', CommentListAPIView.as_view()),
]
