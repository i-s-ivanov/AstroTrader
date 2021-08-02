from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from telescope_shop.accounts.models import Profile

UserModel = get_user_model()


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile


class UserAdmin(BaseUserAdmin):
    inlines = (
        ProfileInlineAdmin,
    )


admin.site.unregister(UserModel)
admin.site.register(UserModel, UserAdmin)
admin.site.register(Profile)
