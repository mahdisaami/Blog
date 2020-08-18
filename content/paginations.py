from rest_framework.pagination import LimitOffsetPagination


class PostListPagination(LimitOffsetPagination):
    max_limit = 10
    default_limit = 5
