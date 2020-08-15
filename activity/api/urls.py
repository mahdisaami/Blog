from django.urls import path

from activity.api.views import LikeAPIVew

urlpatterns = [
    path('like/post <int:pk>', LikeAPIVew.as_view()),
]
