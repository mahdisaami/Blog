from django.urls import path

from relation.api.views import FollowUserAPIView

urlpatterns = [
    path('follow/<str:username>/', FollowUserAPIView.as_view()),
]