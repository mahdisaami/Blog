from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from relation.api.serializers import RelationCreateSerializer, FollowersListSerializer, FollowingsListSerializer
from relation.models import Relation
from relation.paginatinos import FollowersListPagination, FollowingsListPagination

User = get_user_model()


class FollowUserAPIView(CreateAPIView):
    serializer_class = RelationCreateSerializer
    lookup_url_kwarg = 'username'
    lookup_field = 'username'
    queryset = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        target_user = self.get_object()
        if target_user is not None:
            serializer.save(from_user=self.request.user, to_user=target_user)


class FollowersListAPIView(ListAPIView):
    serializer_class = FollowersListSerializer
    queryset = Relation.objects.select_related('from_user').all()
    pagination_class = FollowersListPagination
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()
        qs = queryset.filter(to_user=self.request.user)
        return qs


class FollowingsListAPIView(ListAPIView):
    serializer_class = FollowingsListSerializer
    queryset = Relation.objects.all()
    pagination_class = FollowingsListPagination
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super().get_queryset()
        qs = queryset.filter(from_user=self.request.user)
        return qs
