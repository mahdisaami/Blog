from django.urls import path

from content.api.views import CreatePostAPIView

urlpatterns = [
    path('create/', CreatePostAPIView.as_view()),
]