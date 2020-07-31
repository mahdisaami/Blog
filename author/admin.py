from django.contrib import admin
from django.contrib.auth import get_user, get_user_model

from author.models import Profile


User = get_user_model()


class ProfileAdminInline(admin.TabularInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active')
    list_filter = ("is_superuser",)
    search_fields = ('username', 'id',)
    inlines = (ProfileAdminInline,)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number', 'id')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)