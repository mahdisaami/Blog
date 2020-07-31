from django.urls import path

from author.api.views import RegisterUserAPIView

urlpatterns = [
    path('create/', RegisterUserAPIView.as_view()),

]
