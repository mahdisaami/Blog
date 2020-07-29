from django.contrib import admin

from content.models import Tag, Category, Media, PostTag, Post


class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    search_fields = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')
    search_fields = ('title',)


class MediaAdmin(admin.ModelAdmin):
    list_display = ('post', 'media_type')
    list_filter = ('media_type',)


class MediaAdminInline(admin.TabularInline):
    model = Media


class PostTagAdmin(admin.ModelAdmin):
    list_filter = ('tag', 'post', 'id')
    search_fields = ('title', 'post__title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('get_author', 'title', 'status', 'id')
    list_filter = ('status', 'categories', 'tags')
    search_fields = ('user__username', 'title')
    actions = ('make_publish',)
    inlines = (MediaAdminInline,)

    def get_author(self, obj):
        return obj.user.username

    def make_publish(self, request, queryset):
        queryset.update(status=Post.PUBLISHED)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(user=request.user)

    get_author.short_description = 'user'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(PostTag, PostTagAdmin)
admin.site.register(Post, PostAdmin)
