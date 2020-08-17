from rest_framework.pagination import LimitOffsetPagination


class CommentListPagination(LimitOffsetPagination):
    max_limit = 10
    default_limit = 5
