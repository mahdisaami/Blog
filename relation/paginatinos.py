from rest_framework.pagination import LimitOffsetPagination


class FollowingsListPagination(LimitOffsetPagination):
    max_limit = 10
    default_limit = 5


class FollowersListPagination(LimitOffsetPagination):
    max_limit = 10
    default_limit = 5
