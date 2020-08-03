from django.urls import path

from content.api.views import PostCreateListAPIView

urlpatterns = [
    path('posts/', PostCreateListAPIView.as_view()),
]