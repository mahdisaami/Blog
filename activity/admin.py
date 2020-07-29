from django.contrib import admin
from django.contrib.admin import register

from activity.models import Comment, Like


@register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'id')
    search_fields = ('post__title', 'user__username')


@register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'id')
    search_fields = ('post__title', 'user__username')
