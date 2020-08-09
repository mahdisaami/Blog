from django.urls import path

from author.api.views import RegisterUserAPIView, UserListAPIView

urlpatterns = [
    path('create/', RegisterUserAPIView.as_view()),
    path('list/', UserListAPIView.as_view()),

]
