from django.urls import path

from relation.api.views import FollowUserAPIView, FollowersListAPIView, FollowingsListAPIView

urlpatterns = [
    path('follow/<str:username>/', FollowUserAPIView.as_view()),
    path('followers/', FollowersListAPIView.as_view()),
    path('followings/', FollowingsListAPIView.as_view()),

]
