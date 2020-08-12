from django.urls import path

from author.api.views import RegisterUserAPIView, UserListAPIView, UserRetrieveAPIView

urlpatterns = [
    path('create/', RegisterUserAPIView.as_view()),
    path('list/', UserListAPIView.as_view()),
    path('<str:username>/', UserRetrieveAPIView.as_view()),

]
